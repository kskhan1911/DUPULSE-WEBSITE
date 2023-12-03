from django.shortcuts import render

# Create your views here.
def patient (request):
    return render(request, 'templates_patient/patient.html')
