from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class Collection(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):

    INDICATORS = (
        ('I', 'Important'),
        ('E', 'Keep an eye'),
        ('D', 'Inspiration')
    )

    collection = models.ForeignKey(Collection, null=True, blank=True)
    date = models.DateField()
    description = models.CharField(max_length=255)
    generated_from = models.ForeignKey('self', null=True, blank=True)
    irrelevant = models.BooleanField(default=False)
    indicator = models.CharField(max_length=1, choices=INDICATORS, null=True, blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.description
    

class CompletableItem(Item):
    completed = models.BooleanField(default=False)


class Task(CompletableItem):
    father = models.ForeignKey('self', related_name='childs', null=True, blank=True)


class Event(CompletableItem):
    pass


class Note(Item):
    pass
