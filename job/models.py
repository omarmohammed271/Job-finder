from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField(blank=True,null=True)
    def __str__(self) -> str:
        return self.name
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)    

        
    
def image_upload(instance,filename:str):

    extension = filename.split['.'][1]
    return f'jobs/{instance.job_name}.{extension}'


JOB_TYPE = (
    ('Part Time','Part Time'),
    ('Full Time','Full Time'),
    ('Remote','Remote'),
)


class Job(models.Model):
    job_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50,choices=JOB_TYPE)
    salary = models.IntegerField()
    vacancy = models.IntegerField()
    location = models.CharField(max_length=150)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.job_name)
        super(Job,self).save(*args, **kwargs)  
    
    # how to write clean code