from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.shortcuts import render

def Home(request):

    
    return render(request,"index.html")


def main(request):
    return render(request,'main.html')

def about(request):
        return render(request, 'about.html')


def aboutP(request,id):
    return HttpResponse(id)


def menu(request):
    return render(request,'menu.html')


def contact(request):
    finalre=""
    data={}
    try:
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')

            data={
                'name1':name,
                "email1":email,
                "message1":message,
                "output":finalre
            }

            url = "/thankyou?name={}&email={}&message={}".format(
            name,
            email,
            message
            )
            return HttpResponsePermanentRedirect (url)
    except:
        pass
    return render(request,'contact.html',data)


def galary(request):
    return render(request,'galary.html')


def thankyou(request):
    if request.method=="GET":
        name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')

    data = {
        'name': name,
        'email': email,
        'message': message
    }
    return render(request,'thankyou.html',data)