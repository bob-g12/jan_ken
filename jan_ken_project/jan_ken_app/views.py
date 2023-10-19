from django.shortcuts import render
import random

count = 0
counted = 0
judgment = ["jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html",
            "jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/super.html"]
#ジャンケン結果をランダムにする関数
def random_def(low,high): 
    random_serect = random.randint(low,high)
    return random_serect

#ジャンケンの得点を計算する関数
def point(random_point):
    if judgment[random_point] == "jan_ken/lose.html":
        count = -1
    elif judgment[random_point] == "jan_ken/win.html":
        count = 1
    elif judgment[random_point] == "jan_ken/super.html":
        count = 5
    elif judgment[random_point] == "jan_ken/draw.html":
        count = 0
    return count

#Topページの関数
def frontpage(request):
    context = {
        "count": counted
    }
    return render(request,"jan_ken/lady.html",context)

#ランダムな結果を表示させる関数
def judgpage(request):
    global counted
    random_count = random_def(0,len(judgment)-1)
    
    counted += point(random_count)
    if counted < 10:
        not_clear = "あと"
        clear_count =str(10 - counted)
        not_point = "点"
    else:
        not_clear = ""
        clear_count = "CLEAR"
        not_point = ""
    context = {
        "count": counted,
        "score" : clear_count,
        "limit" : not_clear,
        "point" : not_point
    }
    return render(request,judgment[random_count],context)
