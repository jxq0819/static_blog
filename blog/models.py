from django.db import models


class Article(models.Model):
    # Article unique ID
    article_id = models.AutoField(primary_key=True)
    # Article title
    title = models.TextField()
    # Article brief content
    brief_content = models.TextField()
    # Article main content
    content = models.TextField()
    # Article publish date
    publish_date = models.DateTimeField(auto_now=True)
