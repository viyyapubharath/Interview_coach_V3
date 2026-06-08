
def mock_analyze_answer(answer:str):

    if len(answer) <=20:
        score=6
        feedback="You can do better."

    elif len(answer) >20:
     if len(answe)<=30:
        score=8
        feedback = "Good answer."

    else:
        score=10
        feedback = "Excellent."

    if "%" in answer:
        feedback+="you used measurable impact"

    if (
    "led" in answer.lower()
    or "managed" in answer.lower()
    or "coordinated" in answer.lower()
        ):
    
        feedback += " Demonstrates leadership skills."
    
    return{

        "score":score,
        "feedback":feedback
        }
