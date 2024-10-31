import requests
from bs4 import BeautifulSoup
from typing import List
from transformers import pipeline

def get_content(url: str) -> List[str]:
    response = requests.get(url)
    status = response.status_code

    # Check for status code 200, which indicate good connection
    if status == 200:
        print(f"Successfully scrape {url} with status {status}")
        html = response.content

        soup = BeautifulSoup(html, 'lxml')
        paragraphs = soup.find_all('p')

        # Check if the html contains any <p> tags
        if not paragraphs:
            raise Exception('Error: No <p> tags found')
        else:
            content = []
            for p in paragraphs:
                content.append(p.text)
            return content
        
    # Handling for other status codes which indicate a connection error
    else:
        raise Exception('Error: {}'.format(status))


def clean_content(content: List[str]) -> List[str]:
    return

if __name__ == '__main__':
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    context = """The Nobel Prize week has come and gone, once again reigniting the debate about why so many recipients of this prestigious award are male.

This year, only one Nobel Prize went to a woman — Han Kang, the South Korean author who won the Nobel Prize in Literature for her book The Vegetarian. Meanwhile, all the other prizes — including in the sciences — were awarded to men. But that doesn’t mean women’s research efforts didn’t play a role in the discoveries that earned those men their trophies.

Some people were quick to observe that the work of American biologists Gary Ruvkun and Victor Ambros, who received this year’s Nobel Prize in Medicine for their discovery of microRNAs and their role in gene regulation — an insight that could help combat cancer — was made possible by a string of papers, many of which list Rosalind Lee, Ambros’s wife, as an author. The Nobel Committee even recognised Lee’s contribution on social media, but it apparently wasn’t enough to merit awarding her the prize as well. (And in case you’re wondering, Nobel rules allow for up to three people to be recognised, so that certainly wasn’t the issue.)"""
    question = "List 10 typesof audience would be interested in this context?"
    result = qa_pipeline(question=question, context=context)

    print(result['answer'])