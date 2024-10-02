from fastapi import APIRouter

from models.input_model import Requestmodel
from repository.llm import llmBaseModel
from templates.translate_templates import translate_tepmplate
from templates.grammar_template import grammar_Template
from templates.word_meaning_template import word_meaning_template
from templates.doubts_template import doubts_template
from templates.essay_template import essay_template
from templates.draft_template import draft_template
from typing import List

router = APIRouter()

@router.post("/translate")
def translate(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=translate_tepmplate,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@router.post("/grammar-check")
def grammar_check(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=grammar_Template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@router.post("/word-meaning")
def word_meaning(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=word_meaning_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@router.post("/doubt")
def doubt(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=doubts_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@router.post("/essay")
def essay(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=essay_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e

@router.post("/draft")
def draft(request:Requestmodel):
    # call the funtion fro repository and pass the parameters
    try:
        res =  llmBaseModel(system_instruction=draft_template,request=request)
        print(res)
        return res
    except Exception as e:
        raise e




