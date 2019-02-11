# Django

## 1. 시작하기

1. 프로젝트 시작하기

   ```bash
   $ django-admin startproject 프로젝트이름
   ```

   아래와 같이 프로젝트 구조가 만들어진다.

   ```bash
   ├── db.sqlite3
   ├── django_intro
   │   ├── __init__.py
   │   ├── __pycache__
   │   │   ├── __init__.cpython-36.pyc
   │   │   ├── settings.cpython-36.pyc
   │   │   ├── urls.cpython-36.pyc
   │   │   └── wsgi.cpython-36.pyc
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py
   ```

   ![after adim](/image/django_projet_init-1.PNG)

   지금부터 pwd는 `~/workspace/django_intro`이다

2. 서버 실행하기

   + `setting.py`

     ```python
     ALLOWED_HOST=['*']
     # c9에서는 host - 0.0.0.0, port - 8080만 활용할 수 있기 때문에 위와같이 설정한다.
     ```

   ```bash
   ~/workspace/django_intro $ python manage.py runserver 0.0.0.0:8080
   ```

   그럼 이런 페이지가 나온다!

   ![first page](/image/django_first_runserver.PNG)

   앞으로 모든 장고 명령어는 프로젝트를 만들 때를 제외하고 `python manage.py`를 활용한다.

   따라서, 명령어가 안될 때에는 반드시 `pwd`와 `ls`를 통해서 현재 bash 위치를 확인해보자.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

   ​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

## 2. hello, django

> Django 프로젝트는 여러가지 app의 집합이다.
>
> 각각의 app은 MTV 패턴으로 구성되어 있다.
>
> **MTV** (**M**odel **T**empalte **V**iew) 는 **MVC** (**M**odel(~DB) **V**iew **C**ontroller) 와 상응한다
>
> M(Model) : 어플리케이션의 핵심 로직의 동작을 수행한다.
>
> T (Template) : 사용자에게 결과물을 보여준다.
>
> V (View) : 모델과 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
> **일반적으로 MVC패턴으로 더 많이 사용한다.**
>
>(참고) 장고 구조
>
>  ```
>  ├── project
>  │ ├── app1
>  │ └── app2
>  ```

### 1. 기본로직

앞으로 우리는 1. 요청 url  설정`(url.py)` 2. 처리할 view설정(`views.py`) 3. 결과 보여줄 template 설정(`templates/`)으로 작성할 것이다.



app을 사용하려면 startapp을 해야한다.

![before startapp](/image/before_startapp.PNG)

```bash
$ python manage.py startapp home
```

명령어를 치면 다음과 같이 나온다!

![after startapp](/image/after_startapp.PNG)

1. url 설정

   ```python
   # django-intro/urls.py에 있음
   from django.contrib import admin
   from django.urls import path
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 요청이 home/으로 오면, views의 index함수를 실행시킨다.
       path('home/', views.index),
   ]
   
   ```

   

2. view 설정

   ```python
   # home/viws.py
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse('Hello, Django!')
   ```

   + 주의할 점은 선언된 함쉥서 `request`를 인자로 받아야 한다.
     + request는 사용자(클라이언트)의 정보와 서버에 대한 정보가 담겨있다.

번외.

요청에 대한 정보를 어떻게 넘겨주나요?

```python
def index(request):
    print(request)
    print(type(request))
    print(request.META)
    return HttpResponse('Hello, Django!')
```

하면 터미널창에서 이렇게 뜹니다.

```bash
<WSGIRequest: GET '/home/'>
<class 'django.core.handlers.wsgi.WSGIRequest'>
{'APACHE_PID_FILE': '/home/ubuntu/lib/apache2/run/apache2.pid', 'MANPATH': '/home/ubuntu/.nvm/versions/node/v6.11.2/share/man:/usr/local/rvm/rubies/ruby-2.4.0/share/man:/usr/local/man:/usr/local/share/man:/usr/share/man:/usr/local/rvm/man', 'rvm_bin_path': '/usr/local/rvm/bin', 'C9_SHARED': '/mnt/shared', 'PYENV_ROOT': '/home/ubuntu/.pyenv', 'C9_FULLNAME': 'Jiwon Ashley Ryu', 'GEM_HOME': '/usr/local/rvm/gems/ruby-2.4.0', 'NVM_CD_FLAGS': '', 'APACHE_RUN_USER': 'ubuntu', 'SHELL': '/bin/bash', 'TERM': 'screen', 'IRBRC': '/usr/local/rvm/rubies/ruby-2.4.0/.irbrc', 'SSH_CLIENT': '::ffff:10.240.1.27 41758 22', 'ISOUTPUTPANE': '0', 'NVM_PATH': '/home/ubuntu/.nvm/versions/node/v6.11.2/lib/node', 'C9_PORT': '8080', 'METEOR_IP': '0.0.0.0', 'MY_RUBY_HOME': '/usr/local/rvm/rubies/ruby-2.4.0', 'PHPRC': '/home/ubuntu/workspace', 'PYENV_VERSION': 'django-venv', 'LC_ALL': 'C.UTF-8', 'NVM_DIR': '/home/ubuntu/.nvm', 'USER': 'ubuntu', '_system_type': 'Linux', 'rvm_path': '/usr/local/rvm', 'PYENV_DIR': '/home/ubuntu/workspace/django_intro', 'C9_UID': '2330190', 'PYENV_VIRTUALENV_INIT': '1', 'VIRTUAL_ENV': '/home/ubuntu/.pyenv/versions/3.6.7/envs/django-venv', 'TMUX': '/tmp/tmux-1000/cloud92.2,1117,0', 'PYENV_VIRTUAL_ENV': '/home/ubuntu/.pyenv/versions/3.6.7/envs/django-venv', 'C9_IP': '0.0.0.0', 'rvm_prefix': '/usr/local', 'APACHE_LOG_DIR': '/home/ubuntu/lib/apache2/log', 'PATH': '/home/ubuntu/.pyenv/versions/django-venv/bin:/home/ubuntu/.pyenv/libexec:/home/ubuntu/.pyenv/plugins/python-build/bin:/home/ubuntu/.pyenv/plugins/pyenv-virtualenv/bin:/home/ubuntu/.pyenv/plugins/pyenv-virtualenv/shims:/home/ubuntu/.pyenv/shims:/home/ubuntu/.pyenv/bin:/home/ubuntu/.pyenv/shims:/home/ubuntu/.pyenv/bin:/home/ubuntu/.nvm/versions/node/v6.11.2/bin:/usr/local/rvm/gems/ruby-2.4.0/bin:/usr/local/rvm/gems/ruby-2.4.0@global/bin:/usr/local/rvm/rubies/ruby-2.4.0/bin:/mnt/shared/bin:/home/ubuntu/workspace/node_modules/.bin:/home/ubuntu/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/mnt/shared/sbin:/opt/gitl:/opt/go/bin:/mnt/shared/c9/app.nw/bin:/usr/local/rvm/bin', 'C9_USER': 'ashleyryu', 'HGUSER': 'Jiwon Ashley Ryu', 'NVM_NODEJS_ORG_MIRROR': 'https://nodejs.org/dist', 'PWD': '/home/ubuntu/workspace/django_intro', 'APACHE_RUN_GROUP': 'ubuntu', 'LANG': 'C', 'NODE_PATH': '/mnt/shared/lib/node_modules', 'PYENV_HOOK_PATH': '/home/ubuntu/.pyenv/pyenv.d:/usr/local/etc/pyenv.d:/etc/pyenv.d:/usr/lib/pyenv/hooks:/home/ubuntu/.pyenv/plugins/pyenv-virtualenv/etc/pyenv.d', '_system_arch': 'x86_64', 'TMUX_PANE': '%0', '_OLD_VIRTUAL_PS1': '\\[\\033[01;32m\\]${C9_USER}\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]$(__git_ps1 " (%s)") $ ', '_system_version': '14.04', 'C9_SH_EXECUTED': '1', 'rvm_version': '1.29.2 (latest)', 'PYENV_SHELL': 'bash', 'HOME': '/home/ubuntu', 'SHLVL': '4', 'C9_PID': '6743323', 'GOROOT': '/opt/go', 'LANGUAGE': 'C.UTF-8', 'C9_PROJECT': 'django-intro', 'LOGNAME': 'ubuntu', 'C9_EMAIL': 'ryujw0108@gmail.com', 'GEM_PATH': '/usr/local/rvm/gems/ruby-2.4.0:/usr/local/rvm/gems/ruby-2.4.0@global', 'SSH_CONNECTION': '::ffff:10.240.1.27 41758 ::ffff:172.17.0.43 22', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'GOPATH': '/home/ubuntu/workspace', 'NVM_BIN': '/home/ubuntu/.nvm/versions/node/v6.11.2/bin', 'EMAIL': 'ryujw0108@gmail.com', 'NVM_IOJS_ORG_MIRROR': 'https://iojs.org/dist', 'PORT': '8080', 'METEOR_PORT': '8080', 'IP': '0.0.0.0', 'APACHE_LOCK_DIR': '/home/ubuntu/lib/apache2/lock', 'APACHE_RUN_DIR': '/home/ubuntu/lib/apache2/run', 'C9_HOSTNAME': 'django-intro-ashleyryu.c9users.io', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'RUBY_VERSION': 'ruby-2.4.0', 'rvm_silence_path_mismatch_check_flag': '1', '_system_name': 'Ubuntu', 'BASH_FUNC__gnomeopen%%': '() {  if [ -e "$@" ]; then\n c9 "$@";\n return;\n fi;\n command xdg-open "$@"\n}', 'BASH_FUNC__xdgopen%%': '() {  if [ -e "$@" ]; then\n c9 "$@";\n return;\n fi;\n command xdg-open "$@"\n}', 'DJANGO_SETTINGS_MODULE': 'django_intro.settings', 'TZ': 'Asia/Seoul', 'RUN_MAIN': 'true', 'SERVER_NAME': 'ashleyryu-django-intro-6743323', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8080', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/home/', 'QUERY_STRING': '', 'REMOTE_ADDR': '10.240.1.50', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'django-intro-ashleyryu.c9users.io:8080', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_ACCEPT_LANGUAGE': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'HTTP_COOKIE': '', 'HTTP_X_FORWARDED_PROTO': 'http', 'HTTP_X_FORWARDED_PORT': '80', 'HTTP_X_FORWARDED_FOR': '127.0.0.1', 'HTTP_CONNECTION': 'keep-alive', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x7f1b81375588>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
```



## 3. Template (MTV - T)

> Django에서 활용되는 Template는 DTL(Django Template Language)이다.
>
>  Jinja2와 문법이 유사하다.



1. 요청 urlt 설정

   ```python
   path('home/dinner/', views.dinner)
   ```

   

2. view 설정

   ```python
   def dinner(request):
       box = ['치킨', '초밥', '피자']
       dinner = random.choice(box)
       return render(request, 'dinner.html')
   ```

   + Template를 리턴하면, `render`를 사용하여야 한다.
     + `request`(필수)
     + `template 파일이름`(필수)
     + `template 변수`(선택) : 반드시 `dictionary`타입으로 구성해야 한다.

3. Template 설정

   ```bash
   $ mkdir home/templates
   $ touch home/templates/dinner.html
   ```

   ```html
   <!-- home/templates/dinner.html -->
   <h1>
       {{dinner}}
   </h1>
   ```

## 4. Variable Routing

1. url 설정

   ```python
   path('home/you/<name>', views,you),
   path('home/cube/<int:num>', views.cube),
   ```

2. view 파일 설정

   ```python
   def you(request, name):
       return render(request, 'you.html', {'name' : name})
   ```

   넘겨줄 변수가 두개 이상이면 dict에 넣으면 된다 (ex. {'name' : name, 'age' : age})

3. 템플릿 파일 설정

   ```django
   <h1>
       {{name}}아, 안녕 !
   </h1>
   ```
