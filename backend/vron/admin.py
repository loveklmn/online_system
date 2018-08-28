from django.contrib import admin
from vron.models import Moment, Student, Progress
from vron.models import Page, Sentence, Book
from vron.models import Word, Like, Comment
from vron.models import Notice, Homework
from vron.models import ActiveKey, MatchingGame, JigsawGame, \
	RecognitionGame, ClozeGame

admin.site.register(Moment)
admin.site.register(Student)
admin.site.register(Progress)
admin.site.register(Page)
admin.site.register(Sentence)
admin.site.register(Book)
admin.site.register(Word)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Notice)
admin.site.register(Homework)
admin.site.register(ActiveKey)
admin.site.register(MatchingGame)
admin.site.register(JigsawGame)
admin.site.register(RecognitionGame)
admin.site.register(ClozeGame)
