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