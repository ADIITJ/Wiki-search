import requests
from bs4 import BeautifulSoup
import wikipedia
# Function to search Wikipedia and extract content from the top 5 results
def search_and_extract(query):

    url = f"https://en.wikipedia.org/w/index.php?search={query.replace(' ', '_')}&ns0=1"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = ["https://en.wikipedia.org/"+div.a['href'] for div in soup.find_all('div', class_='mw-search-result-heading')][:3]
        for url in links:
            print(url)
            extract_content(url,query)
        if len(links)==0:
            print('No results found! Try again')
        

# Function to extract content from a Wikipedia page and store it in a text file
def extract_content(url, query):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find("div", class_="mw-parser-output").text
            with open(f"{query.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Content extracted and saved to {query.replace(' ', '_')}.txt")
            extract_chunks(content, query)
        else:
            print("Error: Unable to retrieve content.")
    except Exception as e:
        print("Error:", e)

# Function to extract relevant chunks from the content based on query
def extract_chunks(content, query):
    
    return

# Function to generate the final query for RAG with original query and context
def generate_query(query, context):
    final_query = f"{query} | {context}"
    print("Final query for RAG:", final_query)

def main():
    while True:
        user_input = input("Enter your search query (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        search_and_extract(user_input)

if __name__ == "__main__":
    main()

