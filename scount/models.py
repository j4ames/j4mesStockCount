from django.db import models

class stockcount(models.Model):
    stock_item = models.CharField(unique=True, max_length=30)
    stock_item_quantity = models.IntegerField(null=True)

class stockuserrequest(models.Model):
    request_date = models.CharField(null=True)
    request_requestor = models.CharField(max_length=30)
    request_item = models.CharField(max_length=30)
    request_status = models.CharField(max_length=50, default="Pending")
    request_status_home = models.CharField(max_length=50, default="Pending")
    request_quantity = models.IntegerField(null=True)

class stockpreviousrequest(models.Model):
    request_date = models.CharField(null=True)
    request_item = models.CharField(max_length=30)
    request_status = models.CharField(max_length=50)
    request_quantity = models.IntegerField(null=True)
    request_rejected = models.CharField(max_length=100, default="")

class stocklog(models.Model):
    request_date = models.CharField(null=True)
    request_requestor = models.CharField(max_length=30)
    request_item = models.CharField(max_length=30, unique=False)
    request_status = models.CharField(max_length=30)
    request_quantity = models.IntegerField(null=True)
    request_approvedby = models.CharField(null=True)
    request_rejected = models.CharField(max_length=100, default="")