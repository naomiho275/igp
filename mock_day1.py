#####  Store your name, email, student_id and class_number as STRINGS #####
ind_assign1 = "mock time based practical"
name = "Naomi Ho Ai Hui"
np_email = "S10242585@connect.np.edu.sg"
student_id = "S10242585D"
class_number = "TC01"

# PUT YOUR CODE SOLUTIONS FOR BOTH QUESTIONS INTO ONE PYTHON FILE.
# DON'T NEED TWO SEPARATE PYTHON FILES FOR TWO QUESTIONS. 
# SEPARATE THE CODES WELL BETWEEN QUESTIOS 
# REMEMBER TO INCLUDE COMMENTS TO EXPLAIN YOUR CODE.

# Question 1:

def bp(systolic,diastolic):
    if systolic > 180 or diastolic > 120:
        diagnose= f"Systolic: {systolic} | Diastolic: {diastolic} | Hypertension Crisis"
    elif systolic >=140 or diastolic >=90:
        diagnose= f"Systolic: {systolic} | Diastolic: {diastolic} | Hypertension Stage 2"
    elif systolic >=130 or diastolic >=80:
        diagnose= f"Systolic: {systolic} | Diastolic: {diastolic} | Hypertension Stage 1"
    elif systolic >=120 or diastolic <80:
        diagnose= f"Systolic: {systolic} | Diastolic: {diastolic} | Elevated"
    else:
        diagnose= f"Systolic: {systolic} | Diastolic: {diastolic} | Normal"
    return diagnose

print(bp(134,70))
print(bp(134,80))
print(bp(150,100))
print(bp(181,100))
# try to start from the largest number 

# Question 2: 

def emoticon(mood):
    if mood=="surprise":
        emoji= f"I feel...:o "
    elif mood=="cheeky":
        emoji=f"I feel...;) "
    elif mood=="naughty":
        emoji=f"I feel...:p "
    elif mood=="smiley":
        emoji=f"I feel...:) "
    elif mood=="moody":
        emoji=f"I feel...:( "
    elif mood=="happy":
        emoji=f"I feel...=) "
    else:
        emoji="No such emoticons!"
    
    return emoji

print(emoticon("moody"))




