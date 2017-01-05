from django.shortcuts import render,redirect
from Website.forms import Login,Comment,RegisterForm
from Website.models import NewsManager,News,Comments,Users
from  django.http import Http404,HttpResponseRedirect
import markdown
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_page(request):
    
    if request.method=='GET':
        logform=Login()
    else:
        logform=Login(request.POST)
        if logform.is_vaild():
            clean_data=logform.cleaned_data
    News_list=News.objects.query_by_time()
    ctx={
    'Login_forms':logform,
    'News':News_list,
    }
    return render(request,'Home.html',ctx)
	
def News_Detail_Page(request,News_id):
    try:
        news=News.objects.get(id=News_id)
    except News.DoesNotExist:
        raise Http404('The News do not exist. Please check again!')
    if request.method =='GET':
        comment_form=Comment()
    else:
        comment_form=Comment(request.POST)
        if comment_form.is_valid():
            cleaned_data=comment_form.cleaned_data
            Comments.objects.all().filter(id=News_id).create(**cleaned_data)
            return HttpResponseRedirect('/detail/%s'%(News_id))
    logform=Login()
    Commentlist=Comments.objects.all().filter(id=News_id).order_by('-Create_Date')
    ctx={
    'news':news,
    'Comment':comment_form,
    'Comments':Commentlist,
    'Login_forms':logform,
 }
    return render(request,'News_Detail.html',ctx)
	
#Code login page:
def Log_in(request):
    if request.method=='GET':
        form=Login()
        return render(request,'Login.html',{'form':form})
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():
            username=form.cleaned_data['Name']
            password=form.cleaned_data['Password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                url=request.POST.get('source_url','/')
                return redirect(url)
            else:
                return render(request,'Login.html',{'form':form,'error':'Username or Password do not exist!'})
        else:
            return render(request,'Login.html',{'form':form})

@login_required
def Log_out(request):
    url=request.POST.get('source_url','/')
    logout(request)
    return redirect(url)


def Register(request):
    if request.method=='GET':
        form=RegisterForm()
        return render(request,'Register.html',{'Registerform':form})
    elif request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['Name']
            username2=form.cleaned_data['Name']
            password=form.cleaned_data['Password']
            Profile=form.cleaned_data['Profile']
            user=Users(username=username,password=password,Profile=Profile,Name=username2)
            user.save()
            return redirect('/')
        else:
            return render(request,'Register.html',{'Registerform':form,'error':'Please enter the correct information!'})
       











 