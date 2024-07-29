from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

researcher_task = Task(
    description=(
        'Identify the video {topic} and get detailed information about the video from the channel'
    ),
    expected_output = 'A comprehensive 3 paragraphs long report based on the {topic} of the video content'
    tools = [yt_tool],
    agent = blog_researcher,
)

write_task = Task(
    description=(
        'Get the info from the youtube channel on the topic {topic}'
    ),
    expected_output = 'Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog'
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = False,        ## means we dont want both agents to run in parallel, ie we want them to run sequentially
    output_file = 'new-blog-post.md'

)