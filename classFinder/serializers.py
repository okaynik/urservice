from rest_framework import serializers
from .models import ClassSections

class ClassSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSections
        fields = ('id', 'class_name', 'crn', 'school', 'level',
            'num_units','num_credits','note','passfail','mba')