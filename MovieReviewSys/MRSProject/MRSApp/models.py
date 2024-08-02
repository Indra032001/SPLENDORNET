from django.db import models


class MRSystem(models.Model):
    PUBLISHED = 'Published'
    NOTPUBLISHED = 'NotPublished'

    STATUS_CHOICES = [
        (PUBLISHED, 'Published'),
        (NOTPUBLISHED, 'Notpublished'),
    ]
    CATEGORY_CHOICES = [
        ('horror', 'HORROR'),
        ('action', 'ACTION'),
        ('scifi', 'SCI-FI'),
        ('comedy', 'COMEDY'),
        ('thriller', 'THRILLER'),
    ]
    movietitle = models.CharField(null=False,max_length=200)
    director = models.CharField(null=False,max_length=100)
    reviewcontent = models.CharField(null=False,max_length=100)
    ratings = models.IntegerField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    reviewer_email_id = models.EmailField(unique=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=PUBLISHED,)
    geners = models.CharField(max_length=15,choices=CATEGORY_CHOICES)