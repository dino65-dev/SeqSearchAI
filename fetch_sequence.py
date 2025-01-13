import requests
import streamlit as st

# Define the function to fetch sequence data from NCBI

def fetch_sequence(nucleotide_id, db="protein"):
    """
    Fetches sequence data from NCBI using the EFetch API.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": db,
        "id": nucleotide_id,
        "rettype": "fasta",
        "retmode": "text"
    }
    try:
        with st.spinner("Fetching sequence from NCBI..."):
            response = requests.get(url, params=params)
            response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching sequence: {e}")
        return None