from django.db import models

# Create your models here.

class Sender(models.Model):
    name = models.CharField(max_length=50,default="Anonyme", null=True)
    message_color =models.CharField(max_length=50,default="gray", null=True)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.CharField(max_length=50,null=True)
    sender = models.ForeignKey("Sender", on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.id)+"-->"+self.sender.name
