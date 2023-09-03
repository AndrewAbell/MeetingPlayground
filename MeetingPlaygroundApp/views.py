from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/index.html',context)

def newsletter(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/newsletter.html', context)

def pricing(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/pricing.html')

def resources(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/resources.html', context)

def signup(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/signup.html', context)

def Game(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/Game.html', context)

def GameTwo(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/GameTwo.html', context)

def GameThree(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/GameThree.html', context)

def GameFour(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/GameFour.html', context)

def GameFive(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/GameFive.html', context)

def GameSix(request):
    context = {}
    return render(request, 'MeetingPlaygroundApp/GameSix.html', context)
