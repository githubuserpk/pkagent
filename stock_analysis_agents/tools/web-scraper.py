import requests
from bs4 import BeautifulSoup
from textwrap import dedent

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

text = BeautifulSoup(page.content, "html.parser").text

text = text.replace("\t", "").replace("\r", "").replace("\n", " ")
## text = text.strip('\t\r\n')
print(text)
