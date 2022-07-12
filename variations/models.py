from django.db import models
from books.models import Book


class Variation(models.Model):
    kind = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='variations',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'variations'

    def __str__(self):
        return f'{self.kind}'
