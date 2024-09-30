from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    today = datetime.today().date() # 날짜형 데이터 만들기
    context = {"date":today}
    return render(request, 'foods/index.html', context=context)



