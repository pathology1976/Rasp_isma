import pandas as pd
from datetime import datetime
import arrow 

current_datetime = datetime.now()
current_day = current_datetime.strftime("%A")
current_time = now.format("HH:mm:ss")
print(current_day)
print(current_time)

def idet_para(rasp):
    group = int(input("Какой твой номер группы (введи только цифры): "))
    current_lesson = rasp[
    (rasp['group'] == group) & 
    (rasp['day'] == current_day) & 
    (rasp['start_time'] <= (current_time)) & 
    (rasp['finish_time'] >= (current_time))]
    
    if not current_lesson.empty:
        lesson = current_lesson.iloc[0]["lesson"]
        print(f"У твоей {group} группы идет пара: {lesson}. Поторопись, йобана")
    else: 
        print(f"У {group} группы сейчас нет занятий, иди нахуй.")

rasp = pd.read_csv("rasp.csv", sep="\t")
idet_para(rasp)