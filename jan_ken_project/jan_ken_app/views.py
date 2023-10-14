from django.shortcuts import render

def frontpage(request):
    return render(request,"jan_ken_project/frontpage.html")
