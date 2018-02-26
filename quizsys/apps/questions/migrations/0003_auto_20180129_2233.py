# Generated by Django 2.0 on 2018-01-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20180110_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='instruction',
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(related_name='tags', to='questions.Question'),
        ),
    ]
