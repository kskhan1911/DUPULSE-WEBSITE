from django.shortcuts import render

# Create your views here.
def pharmacy (request):
    return render(request, 'templates_pharmacy/pharmacy.html')
