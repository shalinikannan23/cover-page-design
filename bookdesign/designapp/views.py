from django.shortcuts import render

# Create your views here.

def bookdesign(request):
    return render(request,"designapp/bookdesign.html")