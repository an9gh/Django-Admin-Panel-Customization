from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from .models import JobPost
# Create your views here.

class TempClass:
    x = 5
    


def hello(request):
    list = ["Alpha","Beta"]
    age = [12,45]
    temp = TempClass()
    is_authenticated = False
    context = {
        "name":"Django",
        "first_list":list,
        "temp":temp,
        "age":age,
        "auth":is_authenticated,
        }
    return render(request,"app/hello.html",context)








job_title = [
    "First job",
    "Second job",
    "Third job",
]

job_description = [
    "First Job description",
    "Second Job Description",
    "Third Job Description",
]


# def hello(request):
#     return HttpResponse("<h1>Hello World</h1> <h3>")


def job_list(request):
    # list_of_job = "<ul>"
    
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     print(reverse('job_detail',args = (job_id,)))
    #     list_of_job += f"<li><a href='job/{job_id}'> {j}</a></li>"
    # list_of_job += "</ul>"
    # return HttpResponse(list_of_job)
    jobs = JobPost.objects.all()
    context = {
        "job":jobs
        
    }
    return render(request,"app/index.html",context)


def job_detail(request,id):
    print(type(id))
    
    try:
        if id == 0:
            return redirect(reverse('job_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        job = JobPost.objects.get(id=id)
        context = {"jobb":job,}
        
        return render(request,"app/job_detail.html",context)
    except:
        return HttpResponseNotFound("<h1>Status Code: 404 Not Found</h1>")