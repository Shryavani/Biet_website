from django.db import models


# Create your models here.
class Academic_Calender(models.Model):
    calender = models.FileField(upload_to = 'about_biet/calender/')

    def __str__(self):
        return '{}'.format(self.calender)

# class EOA(models.Model):
#     eoa = models.FileField(upload_to = 'about_biet/eoa/')

#     def __str__(self):
#         return '{}'.format(self.eoa)