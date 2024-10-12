
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
#     api_key=OPENAI_API_KEY
# )

# # test ended



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up...")
    yield
    # Code to run on shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

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
