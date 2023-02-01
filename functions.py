
def calculategrade(markA):
    gradeA='A'
    if markA>=80: 
        gradeA='A'
    elif markA>=75:
        gradeA='B+'   
    elif markA>=70:
        gradeA='B'
    elif markA>=65:
        gradeA='C+'
    elif markA>=60:
        gradeA='C'
    elif markA>=55:
        gradeA='D+' 
    elif markA>=50:
        gradeA='D'
    else : 
        gradeA='F'
    return gradeA
moduleA= input("Please enter the name for module 1: ")
markA= float(input("Please enter the mark for module 1: "))
gradeA=calculategrade(markA)
print(f"Mark for module {moduleA} is {markA}, grade is {gradeA}")

