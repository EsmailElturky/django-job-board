from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Job
from .form import ApplyForm,JobForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs':job_list} 
    return render(request,'job/jobs.html',context)


def job_detail(request,slug):
    job_detail= Job.objects.get(slug=slug)

    if request.method == 'POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myForm=form.save(commit=False)
            myForm.job=job_detail
            myForm.save()
    else:
        form=ApplyForm()

    context = {"job":job_detail ,'form':form}
    return render(request,'job/job_details.html',context)


@login_required
def add_job(request):
    if(request.method=='POST'):
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myForm=form.save(commit=False)
            myForm.owner=request.user
            myForm.save()
            return redirect(reverse('job:job_list'))
    else:
        form=JobForm()

    return render(request,'job/apply_job.html',{'JobForm':form})

