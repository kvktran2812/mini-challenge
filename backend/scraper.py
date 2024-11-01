import requests
from bs4 import BeautifulSoup
from typing import List
import re

def get_content(url: str) -> List[str]:
    response = requests.get(url)
    status = response.status_code

    # Check for status code 200, which indicate good connection
    if status == 200:
        print(f"Successfully scrape {url} with status {status}")
        html = response.content

        soup = BeautifulSoup(html, 'lxml')
        paragraphs = soup.find_all('p')
        content = []

        for p in paragraphs:
            content.append(p.get_text())

        return content
        
    # Handling for other status codes which indicate a connection error
    else:
        raise Exception('Error: {}'.format(status))


def clean_content(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    # Remove special characters from each line using regex
    cleaned_lines = [re.sub(r'[^A-Za-z0-9\s.,!?]', '', line) for line in lines]
    
    # Join cleaned lines back into a single text
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

content = get_content("https://www.businesswire.com/news/home/20241031423444/en/Other-World-Computing-OWC-Helps-Power-the-Future-for-Apple-Users-with-Thunderbolt-5-Solutions-for-New-Mac-Mini-and-MacBook-Pro-with-M4/")
# content = clean_content(content)

print("-------------------------")

for line in content:
    line = clean_content(line)
    print(line)