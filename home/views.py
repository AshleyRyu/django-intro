from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # return HttpResponse(request, 'index.html')
    return render(request, 'index.html')
    
def dinner(request):
    box = ['치킨', '치킨', '롯데리아']
    dinner = random.choice(box)
    '''
    render 필수인자
    1) request, 2) template 파일(html)
    render 선택인자
    3) dictionary : 템플릿에서 쓸 변수 값을 정의
    '''
    
    # return HttpResponse(dinner)
    # return render(request, 'dinner.html') # dinner.html 렌더링해주기
    return render(request, 'dinner.html', {'dinner' : dinner}, {'box' : box}) #인자 넘겨주기
    # template는 기본적로 문법이 jinja2랑 비슷한데 장고에서는 DTL을 쓴다.
    # dDjango Template Language