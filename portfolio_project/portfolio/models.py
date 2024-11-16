from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"message from {self.name}"

