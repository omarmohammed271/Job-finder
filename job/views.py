from django.shortcuts import render
from .models import Job
# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    print(jobs)

    context = {
        'jobs' : jobs,
    }
    return render(request,'jobs/job_list.html',context)