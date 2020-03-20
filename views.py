from django.shortcuts import render

# from django.http import HttpResponse

def index(request):
    # return HttpReponse("<h1> The Main Page</h1>')
    return render(request, 'mainpage.html')
