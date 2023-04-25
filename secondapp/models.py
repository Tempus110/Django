from django.db import models

# 테이블명 -> firstapp+curriculum
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField(null=True)

class Army_shop(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        managed = False
