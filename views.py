
from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'index.html',{'name':'deepak'})

def contact(request):
    return HttpResponse('this is contact page')

def count(request):
        data=request.GET['textarea']
        d=data.split(" ")
        m=len(d)
        dic={'data':data,'size':m}
        
        return render(request,'count.html',{'data':data,'size':m,'dic':dic})
