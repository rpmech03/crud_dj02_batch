from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('addstudent',views.addstudent),
    path('showstudents',views.showstudents),
    path('updatestudent',views.updatestudent),
    path('searchstudent',views.searchstudent),
    path('joinstudent',views.joinstudent),
    path('showjoinstudents',views.showjoinstudents),
    path('updatejoined',views.updatejoined),
    path('searchjoinedstudents',views.searchjoinedstudents),
]