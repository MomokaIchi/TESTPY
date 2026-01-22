import datetime
import time
import random

today = datetime.datetime.now()
# (bad + good + moderate + excellent) should be 100(%)
# o:overall, c:contents
rate_o_b = 3
rate_o_g = 64
rate_o_m = 30
rate_o_e = 3

rate_c_b = 15
rate_c_g = 25
rate_c_m = 30
rate_c_e = 30

# for index
ind_o_b = rate_o_b
ind_o_g = ind_o_b + rate_o_g
ind_o_m = ind_o_g + rate_o_m
ind_o_e = ind_o_m + rate_o_e
ind_c_b = rate_c_b
ind_c_g = ind_c_b + rate_c_g
ind_c_m = ind_c_g + rate_c_m
ind_c_e = ind_c_m + rate_c_e

def overall():
    overall = random.randint(1,100)
    print(f"overall {overall}") # for debug
    if 1 <= overall <= ind_o_b:
        result = "Bad"
    elif  ind_o_b+1 <= overall <= ind_o_g:
        result = "Good"
    elif ind_o_g+1 <= overall <= ind_o_m:
        result = "Moderate"
    elif ind_o_m+1 <= overall <= ind_o_e:
        result = "Excellent"
    else:
        result = "Something went wrong. Check the sum of rate."
    print(f"Overall: {result} luck")
    return overall

def health(overall):
    health = round(random.randint(1,100) * overall / 100)
    # print(f"health point:{health}") # for debug
    if 1 <= health <= ind_c_b:
        point = "★☆☆☆☆"
        comment = "You should pay extra attention to your health now. Make sure to listen to your body's signals, and consider consulting a healthcare professional if needed. It's also important to take time to relax."        
    elif ind_c_b+1 <= health <= ind_c_g:
        point = "★★☆☆☆"
        comment = "You may feel some concerns about your health at this time. It's important to maintain a balanced diet and engage in moderate exercise. Take care of yourself and avoid overexertion."
    elif ind_c_g+1<= health <= ind_c_m:
        point = "★★★☆☆"
        comment = "Your health is generally good, but a bit of caution is necessary. By being mindful of your lifestyle and avoiding excessive stress and unbalanced eating habits, you can achieve even better health."
    elif ind_c_m+1 <= health <= ind_c_e:
        point = "★★★★★"
        comment = "Your health is in excellent condition. You will be able to enjoy your daily life fully and maintain a positive outlook. Pay attention to your exercise and diet to keep up this good condition."
    else:
        point = ""
        comment = "Something went wrong. Check the sum of rate."
    print(f"Health:{point}\n{comment}")
    return health

def study(overall):
    study = round(random.randint(1,100) * overall / 100)
    # print(f"study point:{study}") # for debug
    if 1 <= study <= ind_c_b:
        point = "★☆☆☆☆"
        comment = "Your study luck requires extra attention. You may struggle to concentrate or grasp new concepts. It's a good idea to reassess your study methods and establish a clearer plan. Don't hesitate to ask for guidance from teachers or peers."
    elif ind_c_b+1 <= study <= ind_c_g:
        point = "★★☆☆☆"
        comment = "Your study luck shows some signs of difficulty. You might encounter challenges or distractions that hinder your progress. Stay motivated, seek help when needed, and try to create a conducive study environment."
    elif ind_c_g+1<= study <= ind_c_m:
        point = "★★★☆☆"
        comment = "Your study luck is good, and you will make steady progress. However, you may need to put in a bit more effort to achieve your goals. Stay focused and maintain a consistent study routine, and you will see favorable results."
    elif ind_c_m+1 <= study <= ind_c_e:
        point = "★★★★★"
        comment = "Your study luck is at its peak! You will absorb knowledge quickly and effectively. This is an excellent time to take on new challenges and actively participate in your studies. Success is within your reach!"
    else:
        point = ""
        comment = "Something went wrong. Check the sum of rate."
    print(f"Study:{point}\n{comment}")
    return study

def love(overall):
    love = round(random.randint(1,100) * overall / 100)
    # print(f"love point:{love}") # for debug
    if 1 <= love <= ind_c_b:
        point = "★☆☆☆☆"
        comment = "Your love luck indicates a time of uncertainty. You may feel confused about your feelings or face difficulties in your current relationship. Take time to reflect on what you truly desire in love, and consider seeking advice from trusted friends or loved ones."
    elif ind_c_b+1 <= love <= ind_c_g:
        point = "★★☆☆☆"
        comment = "Your love luck suggests some challenges. Misunderstandings may arise, and patience is key. It's essential to communicate openly and work through any issues. For singles, focus on self-love and personal growth before seeking new relationships."
    elif ind_c_g+1<= love <= ind_c_m:
        point = "★★★☆☆"
        comment = "Your love luck is promising, but there may be some ups and downs. Open communication with your partner will strengthen your relationship. If you're looking for love, be open to opportunities, as meaningful connections are on the horizon."
    elif ind_c_m+1 <= love <= ind_c_e:
        point = "★★★★★"
        comment = "Your love luck is flourishing! If you're single, you may soon encounter someone special. For those in a relationship, your bond will deepen, filled with affection and understanding. This is a wonderful time for romance and connection."
    else:
        point = ""
        comment = "Something went wrong. Check the sum of rate."
    print(f"Love:{point}\n{comment}")
    return love

def check():
    check = input("Do you want to see the points? (if yes, press 'y'):").lower().strip()
    if check == "y" or check == "yes":
        print(f"Overall:{luck_point}%\nHealth:{health_point}%\nStudy:{study_point}%\nLove:{love_point}%")
    elif check == "momo":
        print("Have a nice day! (^-^)b")
    else:
        print("Have a nice day!")

# main
print(f"Today({today.year}-{today.month}-{today.day})'s luck!")
print("Drawing...")
time.sleep(2)
luck_point = overall()
health_point = health(luck_point)
study_point = study(luck_point)
love_point = love(luck_point)
check()
