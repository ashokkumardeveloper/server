from typing import List
from pydantic import BaseModel


class InputModel(BaseModel):
    role: str
    parts: list[str]

class inputString(BaseModel):
    input: str

class Requestmodel(BaseModel):
    history: list[InputModel]
    input: str

class GptRequestModel(BaseModel):
    content:str
    role:str

class OpenAiRequestModel(BaseModel):
    request: List[GptRequestModel]

