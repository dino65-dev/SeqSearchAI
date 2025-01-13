# SeqSearchAI

SeqSearchAI is an advanced AI-powered tool for biological sequence analysis. It allows users to search for accession IDs, fetch sequences from NCBI, perform sequence alignment using BLAST, and interact with an AI model for customized sequence-based insights.

## Features

- **Accession ID Search**: Search for nucleotide or protein accession IDs using NCBI's ESearch API.
- **Sequence Fetching**: Retrieve sequences in FASTA format using NCBI's EFetch API.
- **BLAST Integration**: Perform BLAST searches to find similar sequences in the NCBI database.
- **AI Chat Integration**: Engage in conversations with an AI model to gain insights into the fetched sequences.
- **Sequence Analysis**: Compute GC content, reverse complements, and other properties for nucleotide sequences.
- **User-Friendly Interface**: A clean and interactive web app built with Streamlit.

## Installation

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Biopython](https://biopython.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Cerebras Cloud SDK](https://cerebras.net/)

### Clone the Repository
```bash
$ git clone https://github.com/yourusername/seqsearchAI.git
```

### Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project directory with the following content:

```plaintext
CEREBRAS_API_KEY=your_cerebras_api_key
```

## Usage

### Start the App
Run the Streamlit app:
```bash
$ streamlit run app.py
```

### Using the App
1. **Accession Search**: Enter a query (e.g., gene name or keyword) and select the database (nucleotide or protein) to fetch accession IDs.
2. **Fetch Sequence**: Select an accession ID to retrieve its corresponding sequence.
3. **BLAST Search**: Perform a BLAST search to find similar sequences. The results include alignment details and HSP statistics.
4. **AI Interaction**: Enter your questions or instructions to interact with the AI model based on the fetched sequence.

## Key Technologies
- **Streamlit**: Provides a responsive and user-friendly interface.
- **Biopython**: Enables sequence parsing, BLAST integration, and sequence analysis.
- **NCBI E-Utilities**: Facilitates accession search and sequence retrieval.
- **Cerebras Cloud SDK**: Powers AI-based interactions with high-performance models.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### Steps to Contribute
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add your message here'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- [NCBI E-Utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Cerebras Systems](https://cerebras.net/)
- [Streamlit](https://streamlit.io/)
- [Biopython](https://biopython.org/)

---

Feel free to suggest improvements, report bugs, or ask questions by opening an issue on the GitHub repository.

**Happy Searching!**

