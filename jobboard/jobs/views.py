from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def job_detail(request, pk):
    return render(request, 'edit.html', {"job_id": pk})
