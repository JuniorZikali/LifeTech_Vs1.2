from django.db import models

# Create your models here.
class Administrators(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    surname = models.TextField(db_column='Surname')  # Field name made lowercase.
    mobile_number = models.IntegerField(db_column='Mobile Number')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrators'