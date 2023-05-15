from django.shortcuts import render,redirect
from blog_app.models import signform,add,contactu,proimage,leavecomment,feedback
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import contactform,addform,proimageform,feedbackform
# Create your views here.
@login_required(login_url='login')
def base(request):
    data=add.objects.all()
    return render(request,'base.html',{'data':data})

def about(request):
    return render(request,'about.html')

def feed(request):
    if request.method == 'GET':
        form = feedbackform()
        return render(request,'feed.html',{'form':form})
    else:
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Feedback is saved successfully')
            return redirect('about')
    return render(request,'feed.html')

def home(request):
    data=add.objects.all()
    return render(request,'home.html',{'data':data})
    
    
@login_required(login_url='login')
def index(request):
    data=add.objects.all()
    return render(request,'index.html',{'data':data})

def dele(reuquest,id):
    data=add.objects.get(id=id)
    data.delete()
    return redirect('index')


def update1(request,id):
    data=add.objects.get(id=id)
    print("yes")
    print(data)
    if request.method=='GET':
        form=addform(instance=data)
        return render(request,'update1.html',{'form':form})
    else:
        form=addform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request,'update1.html')
    
@login_required(login_url='login')
def addblog(request):
    if request.method=='GET':
        form=addform()
        return render(request,'addblog.html',{'form':form})
    else:
        form=addform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request,'addblog.html')
@login_required(login_url='login')
def com(request):
    print("in")
    if request.method =="POST":
        print("u")
        user  = request.POST['u_id']
        post = request.POST['post_id']
        comment = request.POST['comment']
        print(comment)
        leavecomment.objects.create(adds_id=user,user_id=post,comment=comment)
        return redirect("readmore",post)
    return render(request,'readmore.html')

def comment(request,id):
    data = leavecomment.objects.filter(user_id=id)
    return render(request,'comment.html',{'data':data})

def deletecomment(request,id,post_id):
    data = leavecomment.objects.get(id=id)
    data.delete()
    return redirect('readmore',id=post_id)

def readmore(request,id):
    data=add.objects.get(id=id)
    data1 = leavecomment.objects.filter(user_id=id)
    
    return render(request,'readmore.html',{'data':data,'data1':data1})

@login_required(login_url='login')
def contact(request):
    if request.method=='GET':
        form=contactform()
        return render(request,'contact.html',{'form':form})
    else:
        form=contactform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showcontact')
        
def showcontact(request):
    data=contactu.objects.all()
    return render(request,'showcontact.html',{'data':data})


@login_required(login_url='login')
def edit(request):
    data=add.objects.filter(created_by=request.user)
    return render(request,'edit.html',{'data':data})


@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        if proimage.objects.filter(user=request.user).exists():
            image = proimage.objects.get(user=request.user)
            da3 = add.objects.filter(created_by=request.user)
            return render(request,'profile.html',{'image':image,'da3':da3})
        else:
            return redirect('profileimage')
    else:
        return redirect("login")


@login_required(login_url='login')
def profileimage(request):
    if request.method=='GET':
        form=proimageform()
        return render(request,'profileimage.html',{'form':form})
    else:
        form=proimageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,'profileimage.html')
    
def deletei(request,id):
    data=proimage.objects.get(id=id)
    data.delete()
    return redirect('profile')

def updatei(request,id):
    data=proimage.objects.get(id=id)
    if request.method=='GET':
        form=proimageform(instance=data)
        return render(request,'profileimage.html',{'form':form})
    else:
        form=proimageform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')   
        return render(request,'profileimage.html')
    
def sign(request):
    if request.method=='POST':
        username=request.POST['username']
        
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']

        if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.success(request,'User name already exists')
                return redirect('login1')
            
            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email-addres is already exists ')
                return redirect('login1')
            else:
                data=User.objects.create_user(username=username,email=email,password=password)
                return redirect('login1')
        else:
            messages.success(request,'Password does not match')

    return render(request,'sign.html')



def showsign(request):
    data=User.objects.all()
    return render(request,'showsign.html',{'data':data})



def delete(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('showsign')

def update(request,id):
    if request.method=='POST':
        username=request.POST['username']
        
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']

        if password==confirm:
            if User.objects.filter(id=id,username=username).exists():
                messages.success(request,'User name already exists')
                return redirect('showsign')
            
            elif User.objects.filter(id=id,email=email).exists():
                messages.success(request,'Email-addres is already exists ')
                return redirect('showsign')
            else:
                data=User.objects.create_user(id=id,username=username,email=email,password=password)
                return redirect('showsign')
        else:
            messages.success(request,'Password does not match')

    return render(request,'sign.html')

# @login_required(login_url='login')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid username/password')
            return redirect('sign')
        else:
            auth.login(request,user)
            return redirect('index')
    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')

def change_p(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_p.html', {'form': form})



@login_required(login_url='login')
def search(request):
    if request.method=='POST':
        search=request.POST['search']
        data=add.objects.filter(title__contains=search)
        return render(request,'search.html',{'data':data})
    else:
        return render(request,'search.html')
    

def filt(request,title):
    print(title)
    dat=add.objects.all().order_by(title)
    return render(request,'filt.html',{'dat':dat})
    






    



