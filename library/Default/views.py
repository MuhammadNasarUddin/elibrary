from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .models import main_cat,category,author,book,status,details,contact,slider,testimonials


# Create your views here.

def about(request):
    return render(request,'aboutus.html')



def contact(request):
    return render(request,'contact.html')


def index(request):
    cat = main_cat.objects.all()
    sli = slider.objects.all()
    aut = author.objects.all()
    catg = category.objects.all()
    bk = book.objects.all()
    ct = {
        'nav': cat,
        'sec': sli,
        'at': aut,
        'cat': catg,
        'book': bk
    }
    return render(request, 'index.html', ct)

def ebooks(request,id):
    cate = main_cat.objects.filter(id=id)
    cat = main_cat.objects.all()
    bk = book.objects.filter(main_cat=id)
    ct = {
        'me': cate,
        'bok': bk,
        'my': cat
    }
    return render(request,'book.html',ct)


def request(request,id):

    print(id)
    xyt=book.objects.filter(id=id)

    for c in xyt:

      abc=details(Email=request.user,status=status.objects.get(id=1),book=c.Name,Url=c.Url,Img=c.Image,Des=c.Desc)
      abc.save()
    messages.success(request, 'Your Request For Download Has Been Forwarded To Admin... Wait For The Approval Thankyou ..!! ')
    return redirect("/profile")


def profile(request):
    current_user = request.user

    mydata = details.objects.filter(Email=current_user, status=status.objects.get(id=2)).values()
    elsedata = details.objects.filter(Email=current_user, status=status.objects.get(id=1)).values()
    #  elsedata = Details.objects.values('id','Email','Status','Book','Img','Des').exclude(Status=Status.objects.get(id=1)).filter(Email=current_user)
    cat = main_cat.objects.all()
    ct = {
        'md': mydata,
        'ed': elsedata,
        'my': cat
    }

    return render(request, 'profile.html', ct)


def delete(request, id):
    print(id)
    details.objects.filter(id=id).update(Status=3)


    return redirect("/profile")
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
        else:
            return render(request,'signup.html',{'form':form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')