from django.db import models

# Create your models here.

class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    #업데이트시에만 컬럼이 수정
    update_at = models.DateTimeField(auto_now=True)
    #만들어질때 컬럼이 수정
    create_at = models.DateTimeField(auto_now_add=True)
