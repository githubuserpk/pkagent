from crewai import Agent
from tools import yt_tool
from groq import Groq
import os 



os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'
OPENAI_API_BASE='https://api.groq.com/openai/v1'


# Create the Groq client
llm = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)



## create a senior blog content researcher ==== an agent
## Agent 1: Blog Researcher

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube videos',
    goal = 'get the relevant video content for the topic{topic} from the Youtube channel',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding youtube videos in Excel Formulas and providing suggestions",
    ),
    llm=llm,
    tools = [yt_tool],
    allow_delegation = True
)

## create a blog writer agent with youtube tool 
## Agent 2: Blog Writer

blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling tech stories about the video {topic}',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft engaging narrations that captivate and educate, bringing new discoveries to light in an accessible manner"
    ),
    llm=llm,
    tools = [yt_tool],
    allow_delegation = False

)


