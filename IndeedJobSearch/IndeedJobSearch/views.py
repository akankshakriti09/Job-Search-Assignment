from django.shortcuts import render, redirect
from api.models import Job
from django.db.models import Q

# Create your views here.


def INDEX(request):
    job = Job.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains=q) | Q(company_name__icontains=q) | Q(company_location__icontains=q))
        try:
            multiple_q |= Q(salary=int(q))
        except ValueError:
            pass            
        job = Job.objects.filter(multiple_q)
    else:
        job = Job.objects.all()

    context = {
        'job' : job
    }

    return render(request, 'index.html', context)


def Edit(request):
    job  = Job.objects.all()

    context = {
        'job' : job,
    }

    return redirect(request, 'index.html',context)

def Update(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        company_location = request.POST.get('company_location')
        salary = request.POST.get('salary')
        
        job = Job(
            id = id,
            title = title,
            company_name =  company_name,
            company_location = company_location,
            salary = salary,         
        )
        job.save()
        return redirect('home')

    return redirect(request, 'index.html')

def Delete(request,id):
    job = Job.objects.filter(id = id)
    job.delete()
    
    context = {
        'job' : job,
    }
    return redirect(('home'))