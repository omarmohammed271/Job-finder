from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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

    extension = filename.split('.')[1]
    return f'jobs/{instance.job_name}.{extension}'


JOB_TYPE = (
    ('Part Time','Part Time'),
    ('Full Time','Full Time'),
    ('Remote','Remote'),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50,choices=JOB_TYPE)
    salary = models.IntegerField()
    vacancy = models.IntegerField()
    description = models.TextField()
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
      
    
def cv_upload(instance,filename:str):
    extension = filename.split('.')[1]
    return f'cv/{instance.name}.{extension}'
class ApplyJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField( max_length=254)
    linkedin = models.URLField(max_length=400)
    cv = models.FileField( upload_to=None, max_length=100)
    cover_letter = models.TextField()

    class Meta:
        verbose_name =("ApplyJob")
        verbose_name_plural =("ApplyJobs")

    def __str__(self):
        return self.name


        
