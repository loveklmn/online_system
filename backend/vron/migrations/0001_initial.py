# Generated by Django 2.1 on 2018-08-13 06:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('pages_num', models.IntegerField()),
                ('assignment', models.TextField()),
                ('guidance', models.TextField()),
                ('read_type', models.CharField(choices=[('IR', 'intensive'), ('ER', 'extensive')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
                ('vote_count', models.IntegerField(default=0)),
                ('level', models.IntegerField()),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Homework')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('picture', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punched', models.BooleanField(default=False)),
                ('current_page', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('audio', models.CharField(max_length=255)),
                ('translated', models.TextField()),
                ('x1', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('x2', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('avatar', models.CharField(max_length=255)),
                ('score', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('audio', models.CharField(max_length=255)),
                ('meaning', models.CharField(max_length=255)),
                ('guidance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Book')),
            ],
        ),
        migrations.AddField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Student'),
        ),
        migrations.AddField(
            model_name='like',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Student'),
        ),
        migrations.AddField(
            model_name='like',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Moment'),
        ),
        migrations.AddField(
            model_name='homework',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Student'),
        ),
        migrations.AddField(
            model_name='homework',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Book'),
        ),
        migrations.AddField(
            model_name='comment',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Student'),
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vron.Moment'),
        ),
    ]
