import random
competition = []
inputing = False
print("")
print("choose wheel mode by inputing number")
print("1. manual")
print("2. prefab list")

inputing1 = input()
if (inputing1 == 1):
    inputing = True
    
    
elif (inputing1 == 2):
    competition = ["", "", "", ""]

while (inputing = True):
    cmpt = input("type value or END to stop adding: ") 
    if (cmpt != "END"):
        competition.append(cmpt)
    else:
        break

ans = random.randint(0, len(competition))
print(f"recieved: {competition[ans]}")