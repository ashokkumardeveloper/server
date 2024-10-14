
# import os
# import re
from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.translate_routes import router
from routes.gpt_routes import gptRouter
 #from templates.translate_templates import translate_tepmplate

# # fro testing
# from openai import OpenAI
# load_dotenv()

# #API_KEY = os.getenv("API_KEY")
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# client = OpenAI(
#     api_key="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"
# )

# from models.input_model import OpenAiRequestModel,GptRequestModel

# # # test ended





@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up...")
    yield
    # Code to run on shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin for development, restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=router,tags=["translate"])
app.include_router(router=gptRouter,tags=['gpt-routes'])

# message = [
#             {
#                 "role":"system",
#                 "content":translate_tepmplate
#             },

#         ]
# message.append({
#     "role":"user",
#     "content":"what is verb",
# })
# message.append({
#     "role":"system",
#     "content":'''
# A verb is a word that describes an action, occurrence, or state of being. Essentially, verbs are the "doing" words in a sentence. For example, in the sentence "She runs every morning," the word "runs" is the verb because it shows the action that she performs.

# Would you like to know more about different types of verbs or how to use them in sentences?''',
# })

# message.append({
#     "role":"user",
#     "content":"yes",
# })


# completion =  client.chat.completions.create(
#     model='gpt-4o-mini',
#     #stream=True,
#     messages= message,
# )

# formatSting = re.sub(r'[\*]', '', completion.choices[0].message.content).strip()

# print(formatSting)
# def openAiLLM(system_instruction:str,request:OpenAiRequestModel):
#     try:
#         message = [
#             {
#                 "role":"Luna",
#                 "content":system_instruction
#             },

#         ]

#         for req in request.request:
#             message.append({
#                 "role": req.role,
#                 "content": req.content
#             })

#         completion =  client.chat.completions.create(
#             model='gpt-4o-mini',
#             #stream=True,
#             messages= message,
#         )

#         print(completion)
#         formatSting = re.sub(r'[\*]', '', completion.choices[0].message.content).strip()
#         res =  {
#             "completion_tokens" : completion.usage.completion_tokens,
#             "prompt_tokens":completion.usage.prompt_tokens,
#             "total_tokens":completion.usage.total_tokens,
#             "messages":formatSting

#         }
#         print(res)
#         return res

#     except Exception as e:
#         print(f"error {e}")
#         return e




#openAiLLM(system_instruction="you are super luna englidh tutor",request=OpenAiRequestModel(request=[GptRequestModel(role="user",content="vanakkam")]))