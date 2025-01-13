from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import os
import requests
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from Bio.SeqUtils import gc_fraction
from Bio.Seq import Seq
import streamlit as st
from fetch_sequence import fetch_sequence
from perform_blast_search import perform_blast_search
from search_accession import search_accession
# Load environment variables
load_dotenv()



# Initialize Cerebras client
client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

# Streamlit app
st.title("SeqSearchAI")

# Sidebar controls
st.sidebar.header("AI Model Settings")
max_tokens = st.sidebar.slider('Max Tokens', 1, 2048, 1024)
temperature = st.sidebar.slider('Temperature', 0.0, 1.0, 0.7)
top_p = st.sidebar.slider('Top P', 0.0, 1.0, 0.9)

# User input for accession search
st.sidebar.header("Search for Accession IDs")
query = st.sidebar.text_input("Enter search query (e.g., gene name or keyword):")
db = st.sidebar.selectbox("Select Database for Search", ["protein", "nucleotide"])
search_results = []

if query:
    search_results = search_accession(query, db=db)
    if search_results:
        st.success(f"Found {len(search_results)} results.")
        selected_id = st.sidebar.selectbox("Select an Accession ID", search_results)
    else:
        st.warning("No results found. Please try a different query.")
else:
    selected_id = None

# Fetch sequence data if ID is selected
sequence = None
if selected_id:
    sequence = fetch_sequence(selected_id, db=db)
    if sequence:
        st.subheader("Fetched Sequence Data")
        st.text(sequence)
        
        # Additional sequence analysis options
        if db == "nucleotide":
            st.subheader("Sequence Analysis")
            seq_obj = Seq("".join(sequence.split("\n")[1:]))
            st.write(f"GC Content: {gc_fraction(seq_obj) * 100:.2f}%")
            st.write(f"Reverse Complement: {seq_obj.reverse_complement()}")

        # Download option
        st.download_button(
            label="Download Sequence",
            data=sequence,
            file_name=f"{selected_id}.fasta",
            mime="text/plain"
        )


# it is not clear what the sequence is, so I will comment it out
# User input for sequence or file upload
#uploaded_file = st.file_uploader("Upload your FASTA file", type="fasta")
#sequence = None

#if uploaded_file is not None:
    # Read sequence from uploaded file
    #seq_record = SeqIO.read(uploaded_file, "fasta")
    #sequence = str(seq_record.seq)


# Perform BLAST Search Integration
if sequence:
    st.subheader("BLAST Search")
    st.warning("This BLAST search only supports nucleotide sequences for now.")
    perform_blast = st.checkbox("Perform BLAST Search", value=False)

    if perform_blast:
        try:
            # Run BLAST search
            blast_result_handle = perform_blast_search(sequence)
            if blast_result_handle:
                st.success("BLAST search completed successfully.")

                # Parse BLAST results
                blast_records = NCBIXML.parse(blast_result_handle)
                for record in blast_records:
                    st.write(f"Query: {record.query}")
                    st.write(f"Database: {record.database}")

                    if record.alignments:
                        st.write(f"Number of alignments: {len(record.alignments)}")
                        for alignment in record.alignments:
                            st.write(f"Alignment title: {alignment.title}")
                            st.write(f"Alignment length: {alignment.length}")
                            for hsp in alignment.hsps:
                                st.write(f"Expect value: {hsp.expect}")
                                st.write(f"Score: {hsp.score}")
                                st.write(f"Identities: {hsp.identities}")
                                st.write(f"Query start: {hsp.query_start}, end: {hsp.query_end}")
                                st.write(f"Subject start: {hsp.sbjct_start}, end: {hsp.sbjct_end}")
                                st.write(f"Query sequence: {hsp.query}")
                                st.write(f"Subject sequence: {hsp.sbjct}")
                                
                    else:
                        st.warning("No alignments found.")
        except Exception as e:
            st.error(f"An error occurred while processing BLAST results: {e}")

# User input for chat
st.header("Chat with AI")
user_input = st.chat_input("Enter your message")

if user_input and sequence:
    # Prepare messages for the AI model
    messages = [
        {
            "role": "system",
            "content": f"You are a helpful AI aware of the following sequence:\n{sequence}"
        },
        {
            "role": "user",
            "content": f'{user_input}'
        }
    ]

    # Generate AI response
    try:
        with st.spinner("Generating AI response..."):
            stream = client.chat.completions.create(
                messages=messages,
                model="llama-3.3-70b",
                stream=True,
                max_completion_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p
            )
            
            # Accumulate chunks of response
            output = ''.join(
                chunk.choices[0].delta.content or ''
                for chunk in stream
            )
        
        # Display the final output
        st.subheader("AI Response")
        st.text(output)
    except Exception as e:
        st.error(f"Error generating response: {e}")
elif user_input and not sequence:
    st.warning("Please provide a valid sequence ID to proceed.")
