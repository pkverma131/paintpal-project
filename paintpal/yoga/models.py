from django.db import models

class YogaPath(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Yogasana(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    beginners_tips = models.TextField()
    benefits = models.TextField()
    cautions = models.TextField()
    variations = models.TextField()
    paths = models.ManyToManyField(YogaPath, through='YogaPathAssociation')

    def __str__(self):
        return self.name

class YogaPathAssociation(models.Model):
    yogapath = models.ForeignKey(YogaPath, on_delete=models.CASCADE)
    yogasana = models.ForeignKey(Yogasana, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['yogapath', 'yogasana']

