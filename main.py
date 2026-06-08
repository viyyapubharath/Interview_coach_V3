from models.schemas import InterviewRequest #calling function request from schema fpr post
from models.schemas import InterviewResponse #calling function response from schema for post

from services.llm_analyzer import llm_analyzer_answer #calling answer form ai to form services

from fastapi import FastAPI #calling fastapi we can use FastAPI,HTTPException also for better understanding i entered in new line
from fastapi import HTTPException # we are using the http exception code for giving the system or sending a universal code like bad request(400) so that system can understand it is an error.

app=FastAPI() #giving the app for the fastapi

@app.get("/") # we are using get 
async def about(): # #async is used for not blocking the other request it will continue the other request 
    return{"MESSAGE":"Welcome"}

@app.post("/analyze") # this is post and for this we use pydantic(basemodel) which is in another file form there we are connected datapipeline
async def analyze(request:InterviewRequest):
    answer=request.answer

    if not answer: # we are using the if answer is not there means if it is empty then raise a error code for that to the fornt end and for user raise details 
        raise HTTPException(
            status_code=400,
            detail="answer is empty"
        )
    if not answer.strip(): #strip will delete the spaces or empty space and give the accurate answer
        raise HTTPException(
            status_code=400,
            detail="answer is empty"
        )

    result= llm_analyzer_answer(answer)

    score=result.get("score")
    feedback=result.get("feedback")

    if score is None:
        return "score is empty : error"
    if feedback is None:
        return "feedback is empty : error"

    if not isinstance(score,int):
        return "score is a string : error" 
    if not isinstance(feedback,str):
        return "feedback is a integer : error"

    return InterviewResponse(
    score=score,
    feedback=feedback
        )
    

    