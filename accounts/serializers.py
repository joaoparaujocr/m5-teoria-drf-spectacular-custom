from pickle import TRUE
from rest_framework import serializers
from datetime import datetime
      
class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    current_date = serializers.SerializerMethodField()
      
    def get_current_date(self, obj):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return date_time