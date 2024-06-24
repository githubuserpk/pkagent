import os
from tavily import TavilyClient


apikey=os.environ.get('TAVILY_API_KEY') 


tavily = TavilyClient(api_key=apikey)
# For basic search:
response1 = tavily.search(query="Should I invest in Apple in 2024?")
print(response1)

# For advanced search:
response2 = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced")
print(response2)

# Get the search results as context to pass an LLM:
# context = [{"url": obj["url"], "content": obj["content"]} for obj in response.results]