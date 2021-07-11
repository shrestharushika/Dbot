from django.urls import path
from .import views 
app_name="bot"

urlpatterns=[
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('form/value/',views.value,name="value")
]
