from django.shortcuts import render

# Create your views here.
def diagnosis (request):
    return render(request, 'templates_diagnosis/diagnosis.html')
