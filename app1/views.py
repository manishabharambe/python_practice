from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
# def setcookie(request):  # this set key values in cookies
#     response = render(request,'cookie.html')
#     response.set_cookie(key='name', value='manisha')
#     response.set_cookie(key='age',value=29 )
#     return response

def homepage(request):
    print(request.COOKIES)      # to see whether home uses cookie or not....yes..it uses  o/p--{'name': 'manisha', 'age': '29'}
    return HttpResponse("hi...welcome to homepage")

def get_cookies(request):
    nm = request.COOKIES.get("name")
    ag = request.COOKIES.get("age")
    print(nm,ag)
    return render(request, 'show_cookies.html')

def delete_cookies(request):
    response = redirect('home')
    response.delete_cookie('name')
    response.delete_cookie('age')
    return response

def set_cookie1(request):
    response = render(request,"cookie.html")
    if request.COOKIES.get('visits'):
        response.set_cookie('data','welcome back')      # overwriting data when hit url again
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits',value + 1)
    else:
        value = 1
        text = "welcome for the first time"
        response.set_cookie('visits',value)
        response.set_cookie('data',text)
    return response

def cookie_session(request):
    print(request.session)
    request.session.set_test_cookie()
    return HttpResponse("<h1>welcome to django session</>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        print("in delete cookie")
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair cookie created")
    else:
        response = HttpResponse("dataflair <br> your bowser does not accept cookie")
    return response

def demo_view(request):
    print(request.session.test_cookie_worked()) # first time will give true
    print(request.session.__dict__) #{'_SessionBase__session_key': 'bss8ahcwgqnc1ab0crxbyp7wdg3a7b9x', 'accessed': False, 
                                        #'modified': False, 'serializer': <class 'django.core.signing.JSONSerializer'>}       
    return HttpResponse("in demo view")

def create_session(request):
    print(request.session.__dict__)
    request.session['name'] = 'manisha'
    request.session['password'] = 'password123'
    request.session['age'] = 25
    request.session['city'] = 'kalyan'
    print(request.session.__dict__)

    return HttpResponse("<h1> dataflair <br> the session is set </>")

# to show session data
def show_session_data(request):
    print(request.session.items())
    return render(request,'session.html')

def delete_session(request):
    print(request.session.items)
    del request.session.get['name']
    del request.session.get['password']
    del request.session.get['age']
    return render(request,'session.html')