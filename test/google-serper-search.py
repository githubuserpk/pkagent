from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY_P6')

tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=5,
)

print(tool.run(search_query="ChatGPT o1 release"))

## https://serper.dev/
