from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=False)
    std = models.CharField(max_length=10, null=False)

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.std)
