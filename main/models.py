from django.db import models

# Create your models here.
from django.db import models
import random


# Create your models here.
class AnnotationBox(models.Model):

    sentence = models.CharField(max_length=2000)
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField(null=True)
    valence = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    arousal = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    rank_idx = models.IntegerField()
    is_annotated = models.BooleanField(default=False)
    is_miscellaneous = models.BooleanField(default=False)
    is_drafted = models.BooleanField(default=False)
    draft_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.sentence

