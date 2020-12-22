from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import MessageForm
from chat.models import message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from profiles.models import Profiles

@login_required
def messager(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.from_user=request.user.username
            instance.save()
    else:
         form = MessageForm()
         print("error")
    return render(request,'chat/chat.html',{'form':form})

@login_required
def MsgView(request,userid):
    val=User.objects.get(username=userid)
    x=User.objects.get(username=request.user.username)
    all_objects= message.objects.filter(Q(to_user=val)&Q(from_user=request.user.username)|Q(to_user=x)&Q(from_user=val)).order_by('time')
    context= {'all_objects': all_objects,'myprofile':x,'userprofile':val}
    return render(request,'chat/chatview.html',context)

@login_required
def listmsg(request):
    val=User.objects.all().exclude(username=request.user.username)
    temp=[]
    x=User.objects.get(username=request.user.username)
    for i in range(0,len(val)):
        y=User.objects.get(username=val[i].username)
        last=message.objects.filter(Q(to_user=y)&Q(from_user=request.user.username)|Q(to_user=x)&Q(from_user=y)).order_by('time').last()
        temp.append([y,last])
    print(temp)
    context={'form':temp}
    return render(request,'chat/list.html',context)
