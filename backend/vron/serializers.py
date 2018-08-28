from rest_framework import serializers
from vron.models import Book, Progress, Page, Notice
from vron.models import Sentence, Word, Homework
from vron.models import Moment, Like, Comment
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','cover', 'level', 'title',
         'pages_num', 'assignment', 'guidance', 'read_type')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = (
            'user',
            'book',
            'punched',
            'current_page',
            'latest_read_time')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('book', 'number', 'picture')

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ('page', 'content', 'audio',
         'translated', 'x1', 'y1', 'x2', 'y2')

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('guidance', 'word', 'meaning')

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('author', 'book', 'created_time', 'content')

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ('homework', 'created_time', 'vote_count', 'level')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('actor', 'target', 'liked')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = ('actor', 'target', 'content')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        field = ('content', 'created_time')
