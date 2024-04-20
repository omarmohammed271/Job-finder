from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Job,ApplyJob
from .forms import ApplyForm

# Create your views here.

# FBV CBV MIxins Generics Viewsets ----> 2 lines
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
@login_required(login_url='accounts:login')
def job_detail(request,slug):
    try:
        job = Job.objects.get(slug=slug)
        if request.method=='POST':
            form = ApplyForm(request.POST,request.FILES)
            if form.is_valid():
                my_form = form.save(commit=False)
                my_form.job = job
                my_form.user= request.user
                my_form.save()
                return redirect('home')
        else:
            form = ApplyForm()
         
             
        

    except Job.DoesNotExist:
        print('Error')
        return HttpResponse('No job with this id')  
    context = {
        'job':job,
        'form':form,
    }
    return render(request,'jobs/job_detail.html',context)


# if request.method=='POST':
        #     name = request.POST['name']
        #     email = request.POST['email']
        #     linkedin = request.POST['linkedin']
        #     cv = request.FILES['cv']
        #     cover_letter = request.POST['cover']

        #     apply_job = ApplyJob.objects.create(
        #         job = job,
        #         name = name,
        #         email=email,linkedin=linkedin,
        #         cv=cv,cover_letter=cover_letter,
        #     )


            # apply_job = ApplyJob()
            # apply_job.job=job
            # apply_job.name = name
            # apply_job.email = email
            # apply_job.linkedin = linkedin
            # apply_job.cv = cv
            # apply_job.cover_letter = cover_letter
            # apply_job.save()   