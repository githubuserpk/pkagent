from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#local gemma2

llm = ChatOllama(
    model="gemma:2b",
    keep_alive=-1,
    temperature=0,
    max_new_tokens=512
)

prompt = ChatPromptTemplate.from_template("Write me a 100 word article on {topic} from the perspective of a {profession}")

chain = prompt | llm | StrOutputParser()
# print(chain.invoke({"topic": "US Elections", "profession": "Indian journalist"}))

for chunk in chain.stream({"topic": "US Elections", "profession": "Indian journalist"}): 
    print(chunk, end="", flush=True)






