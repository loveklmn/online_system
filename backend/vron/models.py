from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField()
    avatar = models.CharField(max_length=255)
    score = models.FloatField()


class Book(models.Model):
    TYPE_OF_READING = (
        ('IR', 'intensive'),
        ('ER', 'extensive')
    )
    cover = models.CharField(max_length=255)
    level = models.IntegerField()
    title = models.CharField(max_length=255)
    pages_num = models.IntegerField()
    assignment = models.TextField()
    guidance = models.TextField()
    read_type = models.CharField(max_length=2, choices=TYPE_OF_READING)


class Progress(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    punched = models.BooleanField(default=False)
    current_page = models.IntegerField()
    latest_read_time = models.DateTimeField(default=datetime.now())


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField()
    picture = models.CharField(max_length=255)


class Sentence(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content = models.TextField()
    audio = models.CharField(max_length=255)
    translated = models.TextField()
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    x2 = models.IntegerField()
    y2 = models.IntegerField()


class Word(models.Model):
    guidance = models.ForeignKey(Book, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    audio = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)


class Homework(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=datetime.now)
    content = models.TextField()


class Moment(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=datetime.now)
    vote_count = models.IntegerField(default=0)
    level = models.IntegerField()


class Like(models.Model):
    actor = models.ForeignKey(Student, on_delete=models.CASCADE)
    target = models.ForeignKey(Moment, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)


class Comment(models.Model):
    actor = models.ForeignKey(Student, on_delete=models.CASCADE)
    target = models.ForeignKey(Moment, on_delete=models.CASCADE)
    content = models.TextField()


class Notice(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(default=datetime.now)
