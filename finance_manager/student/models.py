from django.db import models, migrations

# Create your models here.


class TblStudents(models.Model):
    id_std = models.CharField(primary_key=True, max_length=255)
    name_std = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    class_id = models.CharField(max_length=255, blank=True, null=True)
    hometown = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_students'

