import re
from typing import List
from google import generativeai as genai
import os
from dotenv import load_dotenv
from models.input_model import Requestmodel,OpenAiRequestModel
from openai import OpenAI
load_dotenv()

API_KEY = os.getenv("API_KEY")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def llmBaseModel(system_instruction:str,request:Requestmodel):

    try:
        genai.configure(api_key=API_KEY)

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction= system_instruction
        )

        chat_session = model.start_chat(
history=request.history

        )

        response =  chat_session.send_message(request.input)

        return response.text
    except Exception as e:
        raise e



def openAiLLM(system_instruction:str,request:OpenAiRequestModel):
    try:
        message = [
            {
                "role":"system",
                "content":system_instruction
            },

        ]

        for req in request.request:
            message.append({
                "role": req.role,
                "content": req.content
            })

        completion =  client.chat.completions.create(
            model='gpt-4o-mini',
            #stream=True,
            messages= message,
            max_completion_tokens=1024,
            max_tokens=1024

        )

        print(completion)
        formatSting = re.sub(r'[\*]', '', completion.choices[0].message.content).strip()
        return {
            "completion_tokens" : completion.usage.completion_tokens,
            "prompt_tokens":completion.usage.prompt_tokens,
            "total_tokens":completion.usage.total_tokens,
            "messages":formatSting

        }

    except Exception as e:
        return e


