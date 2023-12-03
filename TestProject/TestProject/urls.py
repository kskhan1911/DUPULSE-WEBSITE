"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from About import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homes'),
    path('patient/', include ('Patient.patient_urls')),
    path('doctor/', include ('Doctor.doctor_urls')),
    path('hospital/', include ('Hospital.hospital_urls')),
    path('diagnosis/', include ('Diagnosis.diagnosis_urls')),
    path('pharmacy/', include ('Pharmacy.pharmacy_urls')),
    path('blood/', include ('Blood.blood_urls')),
    path('organ/', include ('Organ.organ_urls')),
    path('ambulance/', include ('Ambulance.ambulance_urls')),
    path('service/', include ('Service.service_urls')),
    path('payment/', include ('Payment.payment_urls')),
    path('contact/', include ('Contact.contact_urls')),
    path('about/', include ('About.about_urls')),
    path('apps/', include ('Apps.apps_urls')),
    
    path('chatbot', include('chatbot.urls')),
]