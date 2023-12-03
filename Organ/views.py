from django.shortcuts import render

# Create your views here.
def organ (request):
    return render(request, 'templates_organ/organ.html')
