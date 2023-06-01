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
    soup = BeautifulSoup(response.content, 'lxml')  # Get the content of the website
    return soup


def extract_article_content(url):
    """
    Extracts the content of an article from the provided URL.

    :param url: The URL of the article.
    :return: The extracted article content as a string.
    """
    soup = create_soup(url)  # Get the page content of the article
    article = ""
    for news in soup.findAll('div', {'class': 'article-body__content'}):
        article += news.text.strip()  # Extract the article into a string
    return article


def get_today_articles():
    """
    Retrieves a list of articles published today on a specific website.

    :return: A list of article contents.
    """
    nbc_us_url = 'https://www.nbcnews.com/us-news/'
    nbc_url = 'https://www.nbcnews.com/'  # Website URL
    soup = create_soup(nbc_url)  # Get the content of the website

    # Create a list of article links containing articles from today on NBC
    links = []
    for news in soup.findAll('h3',
                             {'class': re.compile(r'styles_headline__5qvTg f5(.*)')}):  # Choose story headlines only
        links.append(news.a['href'])  # Append link of article to list of links
        break

    # Create a list of article contents
    article_contents = []  # A list that contains all the contents
    for link in links:  # Iterate through the links of the different articles to extract their contents separately
        article = extract_article_content(link)
        article_contents.append(article)  # Append the article to the articles list
        break
    return article_contents

# Example usage
# output = get_today_articles()
# print(output[0])
