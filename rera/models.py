from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=512, null=True)
    org_type = models.CharField(max_length=128, null=True)
    address = models.TextField(null=True)
    number = models.CharField(max_length=16, null=True)


class Application(models.Model):
    application_no = models.CharField(max_length=32, primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.TextField()


class RealEstateAgent(models.Model):
    application_no = models.CharField(max_length=32, null=True)
    pan = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=512, null=True)
    org_type = models.CharField(max_length=128, null=True)
    address = models.TextField()
    office_number = models.CharField(max_length=16, null=True)
    mobile = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=128, null=True)
    applications = models.ManyToManyField(Application, related_name='applications', through='RealEstateAgentContract')


class RealEstateAgentContract(models.Model):
    agent = models.ForeignKey(RealEstateAgent, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    amount = models.CharField(max_length=128, null=True)
