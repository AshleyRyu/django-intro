from django.shortcuts import render, HttpResponse
import random
import datetime

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # return HttpResponse(request, 'home/index.html')
    return render(request, 'home/index.html')
    
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
    # return render(request, 'home/dinner.html') # dinner.html 렌더링해주기
    return render(request, 'home/dinner.html', {'dinner' : dinner, 'box' : box}) #인자 넘겨주기
    # template는 기본적로 문법이 jinja2랑 비슷한데 장고에서는 DTL을 쓴다.
    # dDjango Template Language

def you(request, name):
    # name = '지원'
    return render(request, 'home/you.html', {'name' : name})
    # return render(request, 'home/you.html', {'name' : name})

def cube(request, num):
    # num = int(num) # url.py 에서 <int:num>로 넘겨주면 생략가능
    return render(request, 'home/cube.html', {'cube' : num**3})
    # return render(request, 'home/cube.html', {'cube' : num**3})
    
def ping(request):
    return render(request, 'home/ping.html')
    # return render(request, 'home/ping.html')
    
def pong(request):
    # GET방식으로 넘어오는 것들(일종의 딕셔너리)는 얘가 관리한다!
    # 실제 찍어본 출력
    # print(request.GET)
    # <QueryDict: {'message': ['Hi~']}>
    msg = request.GET.get('message')
    return render(request, 'home/pong.html', {'msg' : msg})
    # return render(request, 'home/pong.html', {'msg' : msg})

def user_new(request):
    return render(request, 'home/user_new.html')
    # return render(request, 'home/user_new.html')

def user_read(request):
    print(request.POST.get)
    userid = request.POST.get('id')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_read.html', {'userid' : userid, 'pwd' : pwd})
    # return render(request, 'home/user_read.html', {'userid' : userid, 'pwd' : pwd})

def template_example(request):
    my_dict = {"name" : 'ryu', 'nickname' : 'ashley', 'age': 26}
    my_list = ['짜장면', '짬뽕', '탕수육', '군만두']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    now = datetime.datetime.now()
    return render(request, 'home/template_example.html', {'my_dict' : my_dict, 'my_list' : my_list, 'my_sentence' : my_sentence, 'messages' : messages, 'now' : now})
    # return render(request, 'home/template_example.html', {'my_dict' : my_dict, 'my_list' : my_list, 'my_sentence' : my_sentence, 'messages' : messages, 'now' : now})

def static_example(request):
    # return render(request, 'home/static_example.html')
    return render(request, 'home/static_example.html')
# import random
# from django.shortcuts import render, HttpResponse

# # Create your views here.
# def index(request):
#     print(request)
#     print(type(request))
#     print(request.META)
#     return render(request, 'home/index.html')
    
# def dinner(request):
#     box = ['치킨', '치킨', '편도', '롯데리아']
#     dinner = random.choice(box)
#     # render 필수인자
#     # 1) request,  2) template 파일(html)
#     # render 선택인자
#     # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
#     return render(request, 'home/dinner.html', {'dinner': dinner, 'box': box})
#     # template은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
#     # Django Template Language

# def you(request, name):
#     return render(request, 'home/you.html', {'name': name})