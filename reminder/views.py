from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views import generic as dgv
from django.urls import reverse_lazy
from rest_framework import generics as rgv
from rest_framework import permissions as p
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import AlarmModelSerializer
from .models import AlarmModel

def HomeView(req):
    AlarmModelQuery = AlarmModel.objects.all()
    context = {
        'alarm':AlarmModelQuery
       }
    return render(req , "index.html" , context)

def AlarmsView(req):
    return render(req , "alarms.html")

class APIListAlarmTrueView(rgv.ListAPIView):
    queryset = AlarmModel.objects.all()
    serializer_class = AlarmModelSerializer
    def get_queryset(self):
        queryset = AlarmModel.objects.filter(TimesUp=True)
        return queryset

class APICreateAlarmView(rgv.CreateAPIView):
    serializer_class = AlarmModelSerializer
    # permission_classes = [p.AllowAny]


class APIListAlarmView(rgv.ListAPIView):
    queryset = AlarmModel.objects.all()
    serializer_class = AlarmModelSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = "api/APIListAlarmHtml.html"
    # def get(self, request):
    #     queryset = AlarmModel.objects.all()
    #     return Response({'alarm': queryset})

class APIUpdateDestroyAlarmView(rgv.RetrieveUpdateDestroyAPIView):
    queryset = AlarmModel.objects.all()
    serializer_class = AlarmModelSerializer
    lookup_field = 'id'

class APIDetailAlarmView(rgv.RetrieveUpdateDestroyAPIView):
    queryset = AlarmModel.objects.all()
    serializer_class = AlarmModelSerializer
    def get_queryset(self):
        return AlarmModel.objects.filter(id=self.kwargs["id"])


class ClassBasedUpdateAlarmView(dgv.UpdateView):
    model = AlarmModel
    template_name = 'CRUD/Add-Update.html'
    fields = ("title" , "description","DayHappening","Threshold","CustomPick")
    def get_success_url(self):
        from django.urls import reverse
        return reverse('HomeViewName')

class ClassBasedDeleteAlarmView(dgv.DeleteView):
    model = AlarmModel
    template_name = 'CRUD/Delete.html'
    success_url=reverse_lazy('HomeViewName')

class ClassBasedCreateAlarmView(dgv.CreateView):
    model = AlarmModel
    template_name = 'CRUD/Add-Update.html'
    fields = ("title" , "description","DayHappening","Threshold","CustomPick")
    def get_success_url(self):
        from django.urls import reverse
        return reverse('HomeViewName')