import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

client = Groq( api_key=os.getenv("GROQ_API_KEY") ) #Groq() creates a client that communicates with Groq's API

def test_groq_connection():

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"), #Which LLM should process the request
        messages=[ #Conversation sent to the LLM
            {
                "role": "user", #Message from the user
                "content": "Say hello in one sentence." #Actual prompt
            }
        ]
    )
    return response.choices[0].message.content 
# choices-> Generated response options
# message.content -> Generated text