import requests
import streamlit as st
# Define the function to search for accession IDs

def search_accession(query, db="protein", retmax=10):
    """
    Searches for accession IDs using NCBI's ESearch API.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": db,
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    try:
        with st.spinner("Searching for accession IDs..."):
            response = requests.get(url, params=params)
            response.raise_for_status()
        result = response.json()
        ids = result.get("esearchresult", {}).get("idlist", [])
        return ids
    except requests.exceptions.RequestException as e:
        st.error(f"Error searching for accession IDs: {e}")
        return []