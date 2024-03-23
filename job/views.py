from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Job
# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 2) #(Queryset,number of objects)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(page_obj)
    context = {
        'jobs' : page_obj,
        
    }
    return render(request,'jobs/job_list.html',context)

def job_detail(request,slug):
    try:
        job = Job.objects.get(slug=slug)
    except Job.DoesNotExist:
        print('Error')
        return HttpResponse('No job with this id')  
    context = {
        'job':job,
    }
    return render(request,'jobs/job_detail.html',context)

   