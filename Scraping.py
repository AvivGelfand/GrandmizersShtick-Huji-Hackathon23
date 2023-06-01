from bs4 import BeautifulSoup
import requests
import re


def create_soup(url:str):
    """
    Creates a BeautifulSoup object from the provided URL.

    :param url: The URL of the website.
    :return: The BeautifulSoup object.
    """
    response = requests.get(url)  # Make the HTML request
    soup = BeautifulSoup(response.content, "lxml")  # Get the content of the website
    return soup

def get_today_articles_links(numb_article:int)->list:
    """
    Retrieves a list of articles published today on a specific website.

    :return: A list of article contents.
    """
    nbc_url = "https://www.nbcnews.com/"  # Website URL
    soup = create_soup(nbc_url)  # Get the content of the website

    # Create a list of article links containing articles from today on NBC
    links = []
    # Choose story headlines only
    for i,news in enumerate(soup.findAll("h3", {"class": re.compile(r"styles_headline__5qvTg f5(.*)")})):
        links.append(news.a["href"])  # Append link of article to list of links
        if i==numb_article-1:
            break

    return links

def extract_article_content(url:str)->str:
    """
    Extracts the content of an article from the provided URL.

    :param url: The URL of the article.
    :return: The extracted article content as a string.
    """
    soup = create_soup(url)  # Get the page content of the article
    article = ""
    for news in soup.findAll("div", {"class": "article-body__content"}):
        article += news.text.strip()  # Extract the article into a string
    return article