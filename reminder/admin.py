from django.contrib import admin
from .models import AlarmModel



class AlarmModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'DayHappening' , 'id']

admin.site.register(AlarmModel , AlarmModelAdmin)