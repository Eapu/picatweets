# Generated by Django 2.2 on 2020-07-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(blank=True, max_length=250, null=True)),
                ('tweet_text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
