from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    addres = serializers.CharField(max_length=200)