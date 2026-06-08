import os # it is for operating system
from dotenv import load_dotenv # importing dotenv for reading the env folder data
from fastapi import HTTPException # its a safe check will tranfer the error through universal code to the forntend and everything
import json # json is for converting string into the Dic 
from openai import OpenAI #importing openai for calling llm

load_dotenv() 

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)#assign key

def llm_analyzer_answer(answer):
    response=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system",
            "content":"""
                        you are a interviewer coach analyze
                        the user answer and give a score 0 to 10 
                        Return ONLY valid JSON.
                        Do not add explanations.
                        Do not add markdown.:
                         {
                         "score" : integer from 0 to 10,
                         "feedback":short response or feedback
                         }

                         """},
            
            {"role":"user","content":answer}
        ]
    )
    
    response_text=response.choices[0].message.content
    print("Response Text:", response_text)
    
    try:
        result=json.loads(response_text)
    except Exception:
        raise HTTPException(
        status_code=500,
        detail="Invalid response from AI model"
            )
    return result
    
print(
    llm_analyzer_answer(
        "I led a team of 5 engineers and improved productivity by 20%"
    )
)  
    