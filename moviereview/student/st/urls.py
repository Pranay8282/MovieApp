from django.urls import path
from .import views

urlpatterns=[
    path("<int:st_id>",views.info,name='i')
]