# Generated by Django 3.2.4 on 2021-06-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('summary', models.TextField(help_text='What is what', max_length=1000)),
                ('url', models.CharField(default='Aspirational', help_text='To Store Img', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
    ]
