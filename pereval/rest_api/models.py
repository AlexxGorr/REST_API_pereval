from django.db import models


class PerevalAdded(models.Model):
    ...


class PerevalAreas(models.Model):
    title = models.CharField(max_length=255)
    parent = models.OneToOneField('self', on_delete=models.RESTRICT, null=True)


class PerevalImages(models.Model):
    ...


class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=255)




