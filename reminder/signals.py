from django.db.models import signals as s
from .models import AlarmModel

def PostSaveAlarmSignal(sender , instance , *args, **kwargs):
    if instance:
        if instance.Threshold == "custom pick":
            if not instance.CustomPick:
                instance.Threshold = "10 minutes before"
                instance.save()
        else:
            if instance.CustomPick:
                instance.CustomPick = None
                instance.save()



s.post_save.connect(PostSaveAlarmSignal , sender=AlarmModel)