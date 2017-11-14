from django.db import models


class SecondarySchoolManager(models.Manager):
    def get_queryset(self):
        return super(SecondarySchoolManager, self).get_queryset().filter(mainlevel_code='SECONDARY')


class MixedSchoolManager(models.Manager):
    def get_queryset(self):
        return super(MixedSchoolManager, self).get_queryset().filter(mainlevel_code='MIXED LEVEL')
