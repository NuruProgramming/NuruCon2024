from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
import os


class Speaker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='static/uploads/', null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image:
            ext = self.image.name.split(".")[-1]
            self.image.name = f"{uuid.uuid4()}.{ext}"
        super().save(*args, **kwargs)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    logo = models.FileField(
        upload_to="static/uploads/",
        validators=[FileExtensionValidator(["svg", "png", "jpg", "jpeg"])],
    )
    website = models.URLField()
    description = models.TextField(max_length=500, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.logo:
            ext = self.logo.name.split(".")[-1]
            self.logo.name = f"{uuid.uuid4()}.{ext}"
        super().save(*args, **kwargs)



class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.speaker.title} - {self.speaker.name}"


class MasterOfConference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    image = models.ImageField(upload_to="static/uploads/", null=True, blank=True)

    def __str__(self):
        return self.name
