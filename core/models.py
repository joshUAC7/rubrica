from django.db import models

class Document(models.Model):
    Extension = models.CharField(max_length=50, null=True)
    FileName = models.CharField(max_length=200, null=True)
    Doc_Content = models.BinaryField(null=True)
