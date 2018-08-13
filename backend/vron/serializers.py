from rest_framework import serializers
from vron.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','cover', 'level', 'title',
         'pages_num', 'assignment', 'guidance', 'read_type')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('user', 'book', 'punched', 'current_page', 'latest_read_time')
