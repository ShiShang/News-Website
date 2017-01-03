from django.shortcuts import render
from Website.forms import Login,Comment
from Website.models import NewsManager,News,Comments
from  django.http import Http404
import markdown
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
            cleaned_data['news']=news
            Comments.objects.create(**cleaned_data)
    logform=Login()
    Commentlist=Comments.objects.all().order_by('-Create_Date')
    ctx={
    'news':news,
    'Comment':comment_form,
    'Comments':Commentlist,
    'Login_forms':logform,
 }
    return render(request,'News_Detail.html',ctx)