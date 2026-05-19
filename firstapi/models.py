from django.db import models

# Create your models here.
class Books(models.Model):
    b_name = models.CharField(max_length=50)
    b_price = models.IntegerField()
    b_published_date = models.DateField()

    def __str__(self):
        return self.b_name