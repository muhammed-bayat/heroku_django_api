from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article (models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()


def __str__(self):
    return self.title



# Create your models here.
class Material(models.Model):
    material_name = models.CharField(max_length=200)

    def __str__(self):
        return self.material_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.category_name
    @property
    def get_experiments(self):
        return self.experiment_set.all()
    


class Experiment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = RichTextField()
    video_url = models.URLField()
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
