# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,2)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        return HttpResponse("It is certain")
