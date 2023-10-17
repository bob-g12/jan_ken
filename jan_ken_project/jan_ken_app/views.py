from django.shortcuts import render
import random
judgment = ["jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html",
            "jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/super.html"]
def random_def(low,high):
    random_serect = None
    random_serect = random.randint(low,high)
    return random_serect
def frontpage(request):
    return render(request,"jan_ken/lady.html")
def drawpage(request):
    return render(request,judgment[random_def(0,2)])
def winpage(request):
    return render(request,judgment[random_def(0,2)])
def losepage(request):
    return render(request,judgment[random_def(0,2)])
