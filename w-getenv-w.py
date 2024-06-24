import os
from dotenv import load_dotenv

# Load environment variables from .env file
#load_dotenv()


# Set environment variables
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USERPWD = os.getenv('API_PASSWORD')
print(USERPWD)



print(os.getenv('PATH'))
print(f"os.genv is: {os.getenv('GEMINI_API_KEY')}")     #====option-1


my_key=os.environ.get('GEMINI_API_KEY')                 #====option-2
print(f"os.environ.get(): {my_key}")


#note: option-1 and option-2, both work fine


gq_key=os.environ.get('GROQ_API_KEY')                 
print(f"groq api key: {gq_key}")
