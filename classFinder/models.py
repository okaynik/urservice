from django.db import models

class Class(models.Model):
    meeting_times = models.CharField(max_length=120)
    title_string = models.CharField(max_length=120)
    crn = models.CharField(max_length=120)
    school_abbrv = models.CharField(max_length=120)
    level = models.CharField(max_length=120)
    num_units = models.CharField(max_length=120)
    num_credits = models.CharField(max_length=120)
    notes = models.CharField(max_length=120)
    passfail = models.BooleanField(default=False)
    mba = models.BooleanField(default=False)

    def __str__(self):
        return self.title