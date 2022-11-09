from django.db import models


ThresHoldPick = (
    ("custom pick", "Custom Pick"),
    ("10 minutes before", "10 Minutes Before"),
    ("3 days before", "3 Days Before"),
    ("10 days before", "10 Days Before"),
)

class AlarmModel(models.Model):
    title = models.CharField(max_length=50 , unique=True)
    description = models.TextField(max_length=200,blank=True , null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    DayHappening = models.DateTimeField()
    Threshold = models.CharField(max_length=100,choices=ThresHoldPick , default=ThresHoldPick[1][0])
    CustomPick = models.DateTimeField(blank=True , null=True)
    TimesUp = models.BooleanField(default=False)
    def __str__(self):
        return self.title
