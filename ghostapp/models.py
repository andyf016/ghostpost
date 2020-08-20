from django.db import models
from django.utils import timezone

class Post(models.Model):
    BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))
    boast = models.BooleanField(choices=BOOL_CHOICES, default=False)
    post_content = models.CharField(max_length=140)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    time_stamp = models.DateTimeField(default=timezone.now)

