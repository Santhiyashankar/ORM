from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    noofplayers=models.IntegerField()
    nameoftheplayer=models.CharField(max_length=10)
    age=models.IntegerField()
    noofteams=models.IntegerField()
    noofgoals=models.IntegerField()

class footballplayerAdmin(admin.ModelAdmin):
     list_display=('noofplayers','nameoftheplayer','age','noofteams','noofgoals')

                                                                                        


 
