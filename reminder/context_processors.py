from .models import AlarmModel
from django.utils import timezone


def GlobalAlarm(request):
    alarm = AlarmModel.objects.filter(TimesUp=True)
    return {
        "alarms":alarm
        }


def GlobalAlarmCheck(request):
    current_datetime = timezone.now()
    print(f"current time: {current_datetime}")
    if AlarmModel.objects.filter(TimesUp=False):
        alarm = AlarmModel.objects.filter(TimesUp=False)
        for a in alarm:
            x = a.id
            ala = AlarmModel.objects.get(id=x)
            if ala.CustomPick:
                if current_datetime >= ala.CustomPick:
                    ala.TimesUp = True
                    ala.save()
            elif ala.Threshold == "10 minutes before":
                _10MinutesBefore = ala.DayHappening - timezone.timedelta(minutes=10)
                # print(f"minute: {_10MinutesBefore}")
                # print(f"day: {ala.DayHappening}")
                if current_datetime >= _10MinutesBefore:
                    ala.TimesUp = True
                    ala.save()
            elif ala.Threshold == "3 days before":
                _3DaysBefore = ala.DayHappening - timezone.timedelta(days=3)
                # print(f"minute: {_3DaysBefore}")
                # print(f"day: {ala.DayHappening}")
                if current_datetime >= _3DaysBefore:
                    ala.TimesUp = True
                    ala.save()
            elif ala.Threshold == "10 days before":
                _10DaysBefore = ala.DayHappening - timezone.timedelta(days=10)
                # print(f"minute: {_10DaysBefore}")
                # print(f"day: {ala.DayHappening}")
                if current_datetime >= _10DaysBefore:
                    ala.TimesUp = True
                    ala.save()
            else:
                pass
    if AlarmModel.objects.filter(TimesUp=True):
        alarm = AlarmModel.objects.filter(TimesUp=True)

        for a in alarm:
            x = a.id
            ala = AlarmModel.objects.get(id=x)
            # print(ala.TimesUp)
            if ala.CustomPick:
                if not current_datetime >= ala.CustomPick:
                    ala.TimesUp = False
                    ala.save()
            elif ala.Threshold == "10 minutes before":
                _10MinutesBefore = ala.DayHappening - timezone.timedelta(minutes=10)
                # print(f"minute: {_10MinutesBefore}")
                # print(f"day: {ala.DayHappening}")
                if not current_datetime >= _10MinutesBefore:
                    ala.TimesUp = False
                    ala.save()
            elif ala.Threshold == "3 days before":
                _3DaysBefore = ala.DayHappening - timezone.timedelta(days=3)
                # print(f"minute: {_3DaysBefore}")
                # print(f"day: {ala.DayHappening}")
                if not current_datetime >= _3DaysBefore:
                    ala.TimesUp = False
                    ala.save()
            elif ala.Threshold == "10 days before":
                _10DaysBefore = ala.DayHappening - timezone.timedelta(days=10)
                # print(f"minute: {_10DaysBefore}")
                # print(f"day: {ala.DayHappening}")
                if not current_datetime >= _10DaysBefore:
                    ala.TimesUp = False
                    ala.save()
            else:
                pass
    return {
        "alarmTrue": a
    }