from django.db import models
from django.utils import timezone

class Post(models.Model):
    BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))
    boast = models.BooleanField(choices=BOOL_CHOICES, default=False)
    post_content = models.CharField(max_length=140)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_content

