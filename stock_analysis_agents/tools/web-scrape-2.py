# Import Module
from bs4 import BeautifulSoup
import requests

# Website URL
## URL = 'https://www.geeksforgeeks.org/data-structures/'

URL = "https://realpython.github.io/fake-jobs/"

# Page content from Website URL
page = requests.get(URL)

# Function to remove tags
def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


# Print the extracted data
print(remove_tags(page.content))