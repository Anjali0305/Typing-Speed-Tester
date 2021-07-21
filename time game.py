import matplotlib.pyplot as plt
import time

sec = []
mistakes = 0

print("TYPING SPEED TESTER GAME-")

print("Write 'anjali' for 5 times")

input("Ready?")

for i in range(1,6):
    start = time.time()
    name = input("Enter word---")
    end = time.time()
    sec.append(round(end - start, 2)) 
    print("Time taken to type the word-", str(sec[i-1]), "seconds'")
   
    if name.lower() != 'anjali':
        mistakes += 1 

print("You made", str(mistakes), "mistakes!")
print("Lets see your progress!")
time.sleep(3)

x = ["1st", "2nd", "3rd", "4th", "5th"]
y = sec[:5]  

plt.xlabel("Attempts -->")
plt.ylabel("Time taken in seconds -->")

plt.bar(x,y,color = "lightgreen")
plt.show()