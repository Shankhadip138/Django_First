from django.conf.urls import url
from django.urls import path
from . import views
app_name='mcq'

urlpatterns = [
    path("",views.index,name='index'),
    path('<int:question_id>',views.details,name='details'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
    path('<int:question_id>/results',views.results,name='results'),
    #url(r"^$" , views.index, name='index')
]
