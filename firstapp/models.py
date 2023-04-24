from django.db import models

# 테이블명 -> firstapp+curriculum
class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    # score = models.CharField(max_length=255, null=True)