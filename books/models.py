from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
    )

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f'{self.title}'
