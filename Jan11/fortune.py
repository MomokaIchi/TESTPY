import datetime
import time
import random

today = datetime.datetime.now()


luck_hope = random.randint(1,10)
luck_study = random.randint(1,10)
luck_love = random.randint(1,10)
luck_health = random.randint(1,10)

def luck_overall():
    overall = random.randint(1,100)
    if overall == 1 or 2: # 大吉(excellent luck), 3/100
        print("Luck: Excellent Luck")
    if  3 <= overall <= 40: # 中吉(moderate luck), 38/100
        print("Luck: Moderate Luck")
    if 41 <= overall <= 98: # 吉(good luck), 57/100
        print("Luck: Good Luck")
    if overall == 99 or 100: # 凶(bad luck), 3/100
        print("Luck: Bad Luck")
    else:
        exit



# main
print(f"Today({today.year}-{today.month}-{today.day})'s luck!")

print("Drawing...")
time.sleep(3)
luck_overall()
