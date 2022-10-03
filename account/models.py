from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=True)
    level = models.CharField(max_length=40, null=True)

    class Meta:
        managed = False
        db_table = 'users'