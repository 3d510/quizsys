# Generated by Django 2.0.2 on 2018-02-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_quiz_pass_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionsubmission',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='quizsubmission',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='scoredistribution',
            options={'ordering': ['-created_at']},
        ),
    ]
