from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('meeting_times', 'title_string', 'crn', 'school_abbrv', 'level',
                    'num_units', 'num_credits', 'notes', 'passfail', 'mba')