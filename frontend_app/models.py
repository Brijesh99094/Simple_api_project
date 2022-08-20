from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

class BlogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Blog
        fields = "__all__"
    
