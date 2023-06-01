from datetime import date
from bs4 import BeautifulSoup
import requests
import lxml
import re


def create_soup(url):
    """
    Creates a BeautifulSoup object from the provided URL.

    :param url: The URL of the website.
    :return: The BeautifulSoup object.
    """
    response = requests.get(url)  # Make the HTML request
    soup = BeautifulSoup(response.content, "lxml")  # Get the content of the website
    return soup

def get_today_articles_links():
    """
    Retrieves a list of articles published today on a specific website.

    :return: A list of article contents.
    """
    nbc_url = "https://www.nbcnews.com/"  # Website URL
    soup = create_soup(nbc_url)  # Get the content of the website

    # Create a list of article links containing articles from today on NBC
    links = []
    for news in soup.findAll(
        "h3", {"class": re.compile(r"styles_headline__5qvTg f5(.*)")}
    ):  # Choose story headlines only
        links.append(news.a["href"])  # Append link of article to list of links
    return links

def extract_article_content(url):
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
