from django.shortcuts import render

# Create your views here.
def ambulance (request):
    return render(request, 'templates_ambulance/ambulance.html')
