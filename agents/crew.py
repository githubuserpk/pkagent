from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import researcher_task, write_task

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks = [researcher_task, write_task],
    process = Process.sequential,   ## sequential is default 
    memory = True, 
    cache = True, 
    max_rpm = 100,
    share_crew= True
)


## start task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic: Find Substring Within a String in Excel : MS Excel Tips'})
print(result)

