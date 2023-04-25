from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import Army_shop

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    c = Course(name='데이터 분석', cnt=30)
    c.save()
    c = Course(name='데이터 수집', cnt=20)
    c.save()
    c = Course(name='웹개발', cnt=25)
    c.save()
    c = Course(name='인공지능', cnt=20)
    c.save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
#     result = ''
#     for c in course:
#        result += c.name + '<br>'
#     return HttpResponse(result)
    return render(request, 'secondapp/show.html',{'data' : course})

def army_shop(request):
    army_shop = Army_shop.objects.all()
    return render(request, 'secondapp/army_shop.html',{'army_shop' : army_shop})