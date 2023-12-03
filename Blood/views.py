from django.shortcuts import render

# Create your views here.
def blood (request):
    return render(request, 'templates_blood/blood.html')
