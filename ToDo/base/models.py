from django.db import models
# Create your models here.
class ToDo(models.Model):
    status_list=[('Done','Done'),('Not done','Not done'),('In progress','In progress')]  # this is for the status because status only has limited input(list of choices)
    # and the choices are written in status_list variable twice is because one is for read and one is for write
    name = models.CharField(max_length=200) #this charfield only allows database to store string .
    description =models.TextField() #same thing as charfild but very high length
    status =models.CharField(max_length=50,choices=status_list) #satuts_list is passed to choices
    def __str__(self): #this returns the name which wriiten in line  6....but this is not complsory
        return self.name




 