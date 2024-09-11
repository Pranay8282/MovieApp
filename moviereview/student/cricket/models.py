from django.db import models

# Create your models here.
class States(models.Model):
    player=models.CharField(max_length=50)
    run=models.IntegerField()
    balls=models.IntegerField()
    s4=models.IntegerField()
    s6=models.IntegerField()
    sr=models.FloatField()
    team=models.CharField(max_length=100)
    opponent=models.CharField(max_length=100)

    def __Str__(self):
        return self.player