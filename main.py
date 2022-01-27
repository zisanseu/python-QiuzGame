print("Welcome to my computer Quiz")

playing = input("DO you want to play? ")
print (playing)
if playing.lower() != "yes":
    quit()
print ("okay ! Lets play :)")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
answer = input("what does ALU stand for? ")
if answer.lower() == "arithmetic logic unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct ")
print("You got " + str((score / 5)*100) + " questions correct ")
