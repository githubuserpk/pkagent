import os

from langchain_openai import ChatOpenAI


openai_key=os.environ.get('OPENAI_API_KEY')                 
print(f"openai api key: {openai_key}")

llm = ChatOpenAI(api_key=openai_key, model: str = "gpt-3.5-turbo")



response = llm.invoke("Hello, how are you")
print(response)


chat = ChatOpenAI(
    model_name='gpt-3.5-turbo-16k',
    temperature = self.config.llm.temperature,
    openai_api_key = self.config.llm.openai_api_key,         
    max_tokens=self.config.llm.max_tokens
)


