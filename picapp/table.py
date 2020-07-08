import django_tables2 as tables
from .models import Tweet

class TweetTable(tables.Table):
    class Meta:
        model = Tweet
        template_name = "django_tables2/bootstrap.html"
        fields = ("tweet_id", )