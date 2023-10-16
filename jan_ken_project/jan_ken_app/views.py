from django.shortcuts import render

def frontpage(request):
    return render(request,"jan_ken/lady.html")
def drawpage(request):
    return render(request,"jan_ken/draw.html")
def winpage(request):
    return render(request,"jan_ken/win.html")
def losepage(request):
    return render(request,"jan_ken/lose.html")
