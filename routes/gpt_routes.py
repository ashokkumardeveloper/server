from fastapi import APIRouter

from models.input_model import GptRequestModel
from repository.llm import openAiLLM
from templates.translate_templates import translate_tepmplate
from templates.grammar_template import grammar_Template
from templates.word_meaning_template import word_meaning_template,thanglish_meaning_template
from templates.doubts_template import doubts_template
from templates.essay_template import essay_template
from templates.draft_template import draft_template
from typing import List

gptRouter = APIRouter()

@gptRouter.post("/translate-gpt")
def translate(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=translate_tepmplate,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@gptRouter.post("/grammar-check-gpt")
def grammar_check(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=grammar_Template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@gptRouter.post("/word-meaning-gpt")
def word_meaning(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=thanglish_meaning_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@gptRouter.post("/doubt-gpt")
def doubt(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=doubts_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@gptRouter.post("/essay-gpt")
def essay(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=essay_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@gptRouter.post("/draft-gpt")
def draft(request:GptRequestModel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  openAiLLM(system_instruction=draft_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e




