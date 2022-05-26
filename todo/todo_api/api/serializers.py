from rest_framework import serializers
from todo_api.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "task", "completed", "timestamp", "updated", "user"]
