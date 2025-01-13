import streamlit as st
from Bio.Blast import NCBIWWW

# Define the function to perform a BLAST search

def perform_blast_search(sequence, program="blastn", database="nt"):
    """
    Performs a BLAST search using the given sequence.
    """
    try:
        with st.spinner("Performing BLAST search..."):
            result_handle = NCBIWWW.qblast(program, database, sequence)
        return result_handle
    except Exception as e:
        st.error(f"Error performing BLAST search: {e}")
        return None