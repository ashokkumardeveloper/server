from typing import List
from google import generativeai as genai
import os
from dotenv import load_dotenv

from models.input_model import Requestmodel
load_dotenv()

API_KEY = os.getenv("API_KEY")

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