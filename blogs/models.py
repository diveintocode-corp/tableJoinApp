from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'blogs'

    def __str__(self):
        return f'{self.title}, {self.content}'
