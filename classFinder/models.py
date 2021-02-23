# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClassSections(models.Model):
    id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)
    crn = models.IntegerField()
    school = models.CharField(max_length=10, blank=True, null=True)
    level = models.CharField(max_length=5, blank=True, null=True)
    num_units = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    num_credits = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    note = models.CharField(max_length=500, blank=True, null=True)
    passfail = models.IntegerField()
    mba = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_sections'


class Meetings(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.ForeignKey(ClassSections, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    week_days = models.CharField(max_length=7, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    meeting_type = models.CharField(max_length=45, blank=True, null=True)
    professor = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meetings'
        unique_together = (('id', 'class_field'),)


class Schedules(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'schedules'
        unique_together = (('id', 'users'),)


class SchedulesHasClasses(models.Model):
    schedules = models.OneToOneField(Schedules, models.DO_NOTHING, primary_key=True)
    classes = models.ForeignKey(ClassSections, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'schedules_has_classes'
        unique_together = (('schedules', 'classes'),)


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Users(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'users'
