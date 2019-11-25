from django.shortcuts import render, redirect
from .models import JobPost
from .forms import JobPostForm

def index(request):
    return render(request, 'index.html')

def job_detail(request, pk):
    return render(request, 'edit.html', {"job_id": pk})


def job_add(request):
    if request.method == "POST":
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('/')
    form = JobPostForm()
    return render(request, 'add.html', {'form': form})