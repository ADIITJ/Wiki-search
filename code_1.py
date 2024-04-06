import requests
from bs4 import BeautifulSoup
def search_and_extract(query):
    url = f"https://en.wikipedia.org/w/index.php?search={query.replace(' ', '+')}&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [div.a['href'] for div in soup.find_all('div', class_='mw-search-result-heading')][:3]
        if len(links)==0:
            print('No results found! Try again')
            return
        for url in links:
            title = url.split("/")[-1]
            print(title)
            extract_content(title, query)
    else:
        print("Error in getting webpage")

def extract_content(title, query):
    try:
        wikipedia_url = f"https://en.wikipedia.org/wiki/{title}"
        response = requests.get(wikipedia_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            content_paragraphs = soup.select("p")
            content = "\n".join([paragraph.get_text() for paragraph in content_paragraphs])

            with open("all_content.txt", "a", encoding="utf-8") as f:
                f.write(content)
                f.write("\n")
            print(f"Content extracted and saved to all_content.txt")
        else:
            print(f"Failed to fetch Wikipedia page for '{title}'. Status code: {response.status_code}")

    except Exception as e:
        print("Error:", e)



def main():
    while True:
        user_input = input("Enter the topic about which you want to know (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        search_and_extract(user_input)
    

if __name__ == "__main__":
    main()

