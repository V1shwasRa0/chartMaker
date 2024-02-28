from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class objects2(models.Model):
    obj1 = models.CharField(max_length=30)
    obj2 = models.FloatField()
    def __str__(self):
        return str(self.obj1 + " " + self.obj2)

class ImageModel(models.Model):
    image_field = models.ImageField(upload_to='images') 
    timestamp = models.DateTimeField(auto_now_add=True)

    def delete_all_except_latest():
        # Get the latest record based on the timestamp
        latest_record = ImageModel.objects.latest('timestamp')

        # Delete all records except the latest one
        ImageModel.objects.exclude(pk=latest_record.pk).delete()
