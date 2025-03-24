# Name: E. Kpioyo
# Title: Fortnite Quiz
# Date: March 23, 2025
# Description: This program asks 10 question in a Fortnite quiz and gives a score out of 30 for their score.



print("This is a test to see if you're a true Fortnite fan ")
import time
time.sleep(1)

def sum (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    result = q1+ q2+ q3+ q4+ q5+ q6+ q7+ q8+ q9+ q10
    return result

def q1():
    answer=input("Which Fortnite season had the asteroid: S2 (2), S4 (4), S5 (5), or S6 (6)? ")
    if answer=="4":
        print("Correct")
        return 3
    else:
        time.sleep(1) 
        print("Incorrect")
        return 1

def q2():
    answer2=input("What was the original John Wick skin called: The Shooter (s), The Reaper (r), The John Wick (J), The Gunman (g)? ")
    if answer2=="r":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1
        
def q3():
    answer=input("What town was next to the Wailing Woods? 1. Pleasant Park 2. Greasy Grove 3. Moisty Mire 4. Tomato Town ")
    if answer=="4":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q4():
    answer=input("How much does a Chug Jug heal you by? 1. 50hp 2. 100hp 3. 200hp 4. 1000hp ")
    if answer=="3":
        print("Correct")
        return 3
    else: 
        time.sleep(1) 
        print("Incorrect")
        return 1

def q5():
    answer=input("What was the overpowered shotgun strategy called? 1. Double Pump 2. Shotgun Frenzy 3. Shell Explosion 4. Bullet Storm ")
    if answer=="1":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q6():
    answer=input("Which Fortnite season was space themed? 1. S3 (3)  2. S7 (7) 3. S6 (6) 4. S1 (1) ")
    if answer=="3":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q7():
    answer=input("What is the best OG assault rifle? 1. Scar (s) 2. Burst (b) 3. Tactical (t) 4. Makeshift (m)  ").lower()
    if answer=="s":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q8():
    answer=input("What was the tier 100 skin in season 2? 1. John Wick (j) 2. Black Knight (b) 3. Pheonix (p) 4. Spaceman (s) ").lower()
    if answer=="b":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q9():
    answer=input("Which year was Fortnite BR released? 1. 2017 2. 2019 3. 2018 4. 2016 ")
    if answer=="2017":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1

def q10():
    answer=input("Is Fortnite the greatest game ever? 1. No (n) 2. Eh (e) 3. I guess (i) 4. THE BEST (b) ")
    if answer=="b":
        print("Correct")
        return 3
    else: 
        print("Incorrect")
        return 1
total = sum(q1(),q2(),q3(),q4(),q5(),q6(),q7(),q8(),q9(),q10())

if total <18:
    print("---You aren't a real Fortnite fan---")
elif total <=25:
    print("---You are a semi-fan but could do better---")
else:
    print("---You are a true Fortnite fan!!!!---")

print ("Your score is", total)
