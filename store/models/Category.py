from django.db import models

class Filter(models.Model):
    sort = models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return Filter.objects.all()

    def __str__(self):
        return self.sort