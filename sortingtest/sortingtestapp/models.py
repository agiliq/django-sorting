from django.db import models


class SortableThingy(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(default=10)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.roll)


class SortableThingy2(models.Model):
    parent = models.ForeignKey(SortableThingy)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
