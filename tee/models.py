from django.db import models


class Tee(models.Model):
    qid = models.CharField(max_length=255, null=True)
    havesize = models.CharField(max_length=3, null=True)
    wantsize = models.CharField(max_length=3, null=True)
    havecolor = models.CharField(max_length=10, null=True)
    traded = models.BooleanField(default=False)

    def __str__(self):
        return self.qid

