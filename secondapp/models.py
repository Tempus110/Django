from django.db import models

# 테이블명 -> firstapp+curriculum
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField(null=True)