from . import views
from django.urls import path

urlpatterns = [
    path('',views.hello, name="polls_index"),
    path('bye/',views.index)
]