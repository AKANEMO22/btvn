# Import Module
import random
#Bai 1
a, b = map(int, input().split())
print(random.randint(a, b))
#Bai 2
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
#Bai 3  
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()
#Bai 4
d) b and c are both true
#Bai5
d) ABC Zap ABC
#Bai 6
def computepay(h, r):
    if h > 40:
        pay = (h - 40) * (r * 1.5) + (40 * r)
    else:
        pay = h * r
    return pay
h, r = map(int, input().split())
print(computepay(h, r))
#Bai 7
def check(s):
    if s.isdigit() == False: 
        return False
    else:
        return True  

def computegrade(n):
    if check(n)== False:
        return "Bad Score"
    
    score = float(n)
    if score < 0.0 or score > 1.0:
        return "Bad Score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

n = input()
print(computegrade(n))