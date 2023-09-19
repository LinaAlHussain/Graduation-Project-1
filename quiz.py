import time

Major = "CPE"
Course = "Graduation Project"
IDE = "VS Code"
Language = "Python"

score = 0  

print("Please enter your major: ")
start_time = time.time()  
m = input()
end_time = time.time()  

if m == Major:
    print("Correct!")
    score += 1 
else:
    print("Incorrect, try again :)")

elapsed_time = end_time - start_time
print("Time taken for question 1: " + "{:.2f}".format(elapsed_time) + " seconds\n")

print("Now enter the course name: ")
start_time = time.time()
c = input()
end_time = time.time()

if c == Course:
    print("Correct!")
    score += 1
else:
    print("What? Of course not!")

elapsed_time = end_time - start_time
print(f"Time taken for question 2: {elapsed_time:.2f} seconds\n")

print("Where do you work (IDE)?: ")
start_time = time.time()
id = input()
end_time = time.time()

if id == IDE:
    print("Well done!")
    score += 1
else:
    print("Hmmmm, really?")

elapsed_time = end_time - start_time
print(f"Time taken for question 3: {elapsed_time:.2f} seconds\n")

print("What is the programming language you used?: ")
start_time = time.time()
L = input()
end_time = time.time()

if L == Language:
    print("Correct!")
    score += 1
else:
    print("I don't think so")

elapsed_time = end_time - start_time
print(f"Time taken for question 4: {elapsed_time:.2f} seconds\n")

print("Your score is: " + str(score) + " out of 4")  