"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Translate the provided Tamil or Thanglish sentence to English. Ensure that you fully understand the original sentence's context, tone, and nuances. The translation should be professional, capturing the intended meaning without any alterations. Avoid providing explanations or any additional text; deliver only the translated sentence\n",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "vanakkam",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hello \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "unakku ippo ennathaanda venu",
      ],
    },
    {
      "role": "model",
      "parts": [
        "What do you want now? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "vaaya moodittu iru konja neram",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Just",
      ],
    },
    {
      "role": "user",
      "parts": [
        "konja neram vaaya moodittu iru da",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Shut up",
      ],
    },
    {
      "role": "user",
      "parts": [
        "evlo neranda wait pandrathu",
      ],
    },
    {
      "role": "model",
      "parts": [
        "How long should I wait? \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ennale mudiyala",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can't do it. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "eppa saamy onnu sollale vidu",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please tell me something now. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ennathanda uh prachana? yenda ipd pannittu irukke",
      ],
    },
    {
      "role": "model",
      "parts": [
        "What's your problem? Why are you acting like this? \n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "nee poniya\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Go",
      ],
    },
    {
      "role": "user",
      "parts": [
        "nee anga poniya",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Go there. \n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "nee anga ponaya",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Did you go there? \n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "ponaya",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Did you go? \n\n\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)