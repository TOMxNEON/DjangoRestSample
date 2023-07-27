from rest_framework import serializers

from .models import Task
import re



class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_done', 'uid']

    def validate(self, validated_data):
        if validated_data.get('title'):
            task_title = validated_data['title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if regex.search(task_title):
                raise serializers.ValidationError('Title cannot contain special characters')
                
            if len(task_title) < 3:
                raise serializers.ValidationError('Title cannot shorter than 3 characters')
                
        return validated_data