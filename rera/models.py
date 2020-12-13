from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=512)
    org_type = models.CharField(max_length=128)
    address = models.TextField()
    number = models.CharField(max_length=16)


class Application(models.Model):
    application_no = models.CharField(max_length=32, primary_key=True)


class RealEstateAgent(models.Model):
    application_no = models.CharField(max_length=32)
    pan = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=512)
    org_type = models.CharField(max_length=128)
    address = models.TextField()
    office_number = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)
    email = models.CharField(max_length=128)
    applications = models.ManyToManyField(Application, related_name='applications', through='RealEstateAgentContract')


class RealEstateAgentContract(models.Model):
    agent = models.ForeignKey(RealEstateAgent, on_delete=models.CASCADE)
    application_no = models.ForeignKey(Application, on_delete=models.CASCADE)
