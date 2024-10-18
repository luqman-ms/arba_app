from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)