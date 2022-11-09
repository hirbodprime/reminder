from django.urls import path
from . import views as v


urlpatterns = [
    path('' , v.HomeView , name="HomeViewName"),
    path('alarms/', v.AlarmsView, name="AlarmsViewName"),
    path('my-reminders/create/', v.ClassBasedCreateAlarmView.as_view(), name="CreateViewName"),
    path('my-reminders/update/<int:pk>/',v.ClassBasedUpdateAlarmView.as_view() ,name="UpdateViewName"),
    path('my-reminders/delete/<int:pk>/', v.ClassBasedDeleteAlarmView.as_view(), name="DeleteViewName"),
    path('my-reminders/api/create/' , v.APICreateAlarmView.as_view()),
    path('my-reminders/api/list/alarms/', v.APIListAlarmTrueView.as_view()),
    path('my-reminders/api/list/', v.APIListAlarmView.as_view()),
    # path('my-reminders/api/detail/<int:id>' , v.APIDetailAlarmView.as_view()),
    path('my-reminders/api/RUD/<int:id>/' , v.APIUpdateDestroyAlarmView.as_view()),

]