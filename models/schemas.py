from pydantic import BaseModel

class InterviewRequest(BaseModel):
    answer:str

class InterviewResponse(BaseModel):
    score:int
    feedback:str
