# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    number = models.AutoField(db_column='Number', primary_key=True)  # Field name made lowercase.
    артикул = models.TextField(db_column='Артикул', blank=True, null=True)  # Field name made lowercase.
    наименование_ru = models.TextField(db_column='Наименование RU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    наименование_en = models.TextField(db_column='Наименование EN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    наименование_de = models.TextField(db_column='Наименование DE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hs = models.TextField(db_column='HS', blank=True, null=True)  # Field name made lowercase.
    описаине = models.TextField(db_column='Описаине', blank=True, null=True)  # Field name made lowercase.
    вес_нетто = models.TextField(db_column='Вес нетто', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unnamed_8 = models.TextField(db_column='Unnamed: 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image1 = models.TextField(blank=True, null=True)
    image2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Products'
