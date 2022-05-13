from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    img = models.ImageField()


class Info(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    name = models.CharField(max_length=255)
    img = models.ImageField()



class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    img = models.ImageField()


class Others(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()


class AboutUs(models.Model):
    logo = models.ImageField(upload_to="AboutUs/")
    location = models.CharField(max_length=300)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)


class ContactUS(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    description = models.TextField()

class Newsletter(models.Model):
    email = models.EmailField()


class PracticesAreas(models.Model):
    flatication = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    text1 = models.CharField(max_length=150)
    text2 = models.TextField()


class OurExpertise(models.Model):
    title = models.CharField(max_length=80)
    img = models.ImageField(upload_to="OurExpertise/")
    

class Flatication(models.Model):
    expertise = models.ForeignKey(OurExpertise, on_delete=models.CASCADE)
    flatication = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=150)