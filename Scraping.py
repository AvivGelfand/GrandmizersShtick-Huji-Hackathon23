from datetime import date
from bs4 import BeautifulSoup
import requests
import lxml
import re

def create_soup(link):
    r = requests.get(link) # make the HTML request
    soup = BeautifulSoup(r.content,'lxml') # Get the content of the website
    return soup

def return_list_of_articles():

    nbc_us_url = 'https://www.nbcnews.com/us-news/'
    nbc_url = 'https://www.nbcnews.com/' # Websit URL
    soup = create_soup(nbc_url) # Get the content of the website

    # Create a list of article links containing articles from today on NBC
    links = []
    for news in soup.findAll('h3',{'class':re.compile(r'styles_headline__5qvTg f5(.*)')}): # Choose story headlines only
        links.append(news.a['href']) # append link of article to list of links

    # Create a list of article contents
    article_contents = [] # a list that contains all the contents
    for link in links: # iterate through the links of the different articles to extract their contents seperately
        article = extract_article_content(link)
        article_contents.append(article) # append the article to the articles string
    return article_contents

def extract_article_content(link):
    soup = create_soup(link)  # Get the page content of the article
    article = ""
    for news in soup.findAll('div', {'class': 'article-body__content'}):
        article += news.text.strip()  # extract the article into a string
    return article




articles = return_list_of_articles()
print(articles[0])
print(articles[1])