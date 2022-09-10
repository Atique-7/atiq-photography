from django.db import models
from .Category import Filter

# Create your models here.
class Picture(models.Model):
    piece = models.ImageField(upload_to='items/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=250, default="")
    sort = models.ForeignKey(Filter, on_delete=models.CASCADE, default=1)
    permalink = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_pieces():
        return Picture.objects.all()

    @staticmethod
    def get_all_pieces_by_sort(sort_id):
        if sort_id:
            return Picture.objects.filter(sort=sort_id)
        else:
            return Picture.get_all_pieces()

    @staticmethod
    def getProductsbyId(ids):
        return Picture.objects.filter(id__in=ids)
