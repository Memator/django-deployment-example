from django.urls import path, include
from . import views

#TEMPALTE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path("relative/",views.relative,name='relative'),
    path("other/",views.other,name="other")
]