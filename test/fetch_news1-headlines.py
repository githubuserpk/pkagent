import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'q=Google&'
       'pageSize=5'
       'from=2024-08-10&'
       'sortBy=popularity&'
       'apiKey=8bed1e3fc5914c54ba04a57224fbcc29')

response = requests.get(url)
data = response.json()
print(data)

if 'articles' in data:
    for article in data['articles']:
        print(article['title'])
        print(article['description'])
        # ... other fields
else:
    print("No articles found.")
