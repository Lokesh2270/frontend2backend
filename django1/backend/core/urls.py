from django.urls import path
from . import views
urlpatterns=[
    path('app/loki',views.loki,name="loki")
]