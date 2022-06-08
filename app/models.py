import email
from django.db import models
from cloudinary.models import CloudinaryField

class Blogs(models.Model):
    image = CloudinaryField('image')
    heading = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=False)

    def __str__(self):
        return self.heading

class Reply(models.Model):
    comment = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=256, null=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return self.comment

class Comment(models.Model):
    comment = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=256, null=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name="message")


    def __str__(self):
        return self.comment

class MailingList(models.Model):
    email = models.CharField(max_length=250, blank=False)
    isSubscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email