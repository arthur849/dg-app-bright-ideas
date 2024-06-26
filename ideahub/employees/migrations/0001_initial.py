# Generated by Django 4.2.13 on 2024-06-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('dep', models.TextField(max_length=30, null=True)),
                ('birthdate', models.CharField(max_length=30, null=True)),
                ('salary', models.TextField(max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100, null=True)),
                ('thumbsUppCount', models.IntegerField(null=True)),
                ('thumbsDownCount', models.IntegerField(null=True)),
                ('idea', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
