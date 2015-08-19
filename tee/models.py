from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.size


class Tee(models.Model):
    qid = models.CharField(max_length=255, null=True)
    havesize = models.ForeignKey(Size, related_name='havesize', null=True)
    wantsize = models.ForeignKey(Size, related_name='wantsize', null=True)
    havecolor = models.CharField(max_length=10, null=True)
    traded = models.BooleanField(default=False)

    def __str__(self):
        return self.qid

