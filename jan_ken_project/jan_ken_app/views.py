from django.shortcuts import render
import random

count = 0
counted = 0
judgment = ["jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html",
            "jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/super.html"]
def random_def(low,high):
    random_serect = random.randint(low,high)
    return random_serect

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

def frontpage(request):
    context = {
        "count": counted
    }
    return render(request,"jan_ken/lady.html",context)
def judgpage(request):
    global counted
    random_count = random_def(0,len(judgment)-1)
    
    counted += point(random_count)
    
    context = {
        "count": counted
    }
    print(counted)
    return render(request,judgment[random_count],context)
