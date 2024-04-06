# Wiki-search to generate prompt with RAG

Welcome to the WIKI SEARCH! This tool combines **web scraping** with natural language processing technique called **RAG[Retrieval Augmented Generation]** to provide enhanced prompts for question answering systems.

## Overview

The project extracts pertinent information from the top three search results on Wikipedia, which is then fed into the RAG Prompt Generator for preprocessing and generating prompts for question answering systems. It comprises two key components:

1. **Web Scraping**: Utilizing only the BeautifulSoup library, the `search_and_extract` function queries Wikipedia for relevant articles based on user input. It subsequently extracts content from the top search results and stores it in a text file.

2. **Natural Language Processing**: The `RAG.py` module handles the preprocessing of the extracted text and generates prompts using the Retrieval-Augmented Generation (RAG) technique. It segments the text into chunks, identifies similar sentences, and constructs prompts based on user queries. Further details and code implementation for RAG can be found in the project repository at [GitHub](https://github.com/ADIITJ/RAG_implementation).

## Features

- **Dynamic Web Scraping**: Automatically fetches content from Wikipedia based on user input.
- **Customizable Chunking**: Allows users to specify the number of sentences per chunk and the number of chunks.
- **RAG Prompt Generation**: Generates prompts with contextual information, improving the accuracy of question answering systems.

## How to Use

1. **Installation**: 
   - Ensure you have Python installed on your system.
   - Install the required libraries by running `pip install -r requirements.txt`.

2. **Run the Program**: 
   - Execute the `wiki.py` script by running `python wiki.py`.
   - Follow the on-screen instructions to enter a topic of interest.
   - The program will fetch relevant content from Wikipedia and generate prompts.

3. **Customization**: 
   - Adjust the number of sentences per chunk and the number of chunks in the `wiki.py` script to customize the prompts according to your requirements.
4. **Creation and deletion of context**:
   - All the context taken from wikipedia pages is deleted after the user exits the chat by saying 'bye'

## Usage

```bash
python wiki.py
```
But in this we further have to input:
-  `topic`: A specific subject or theme for which you want to generate a prompt
- `sentences_per_chunk`: Number of sentences per chunk for chunking the text data.
- `num_chunks`: Number of chunks to generate prompts from.

## Example

```bash
python wiki.py
```
and you further input 'python programming'  3 and 5, then it will fetch top 3 pages related to "python programming" from Wikipedia, breaks it into chunks of 3 sentences each, and generates prompts consisting of 5 chunks.

## Author

Both the programs have been developed by me. For any inquiries or feedback, please contact [b22ai045@iitj.ac.in].