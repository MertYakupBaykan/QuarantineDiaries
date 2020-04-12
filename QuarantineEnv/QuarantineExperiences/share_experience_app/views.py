from django.shortcuts import render
from django.views import generic
from share_experience_app.forms import UserForm
from .models import ExperienceItem,Like
#login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    items = ExperienceItem.objects.all()
    return render(request,'index.html',{'items': items})

def post_detail(request, experience_id):
    item_to_display = ExperienceItem.objects.get(id=experience_id)
    return  render(request,'post_detail.html',{'experience':item_to_display})

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('user_password')

            user = authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("Account Not Active")
            else:
                return HttpResponseRedirect('signin')
        else:
            return render(request,'signin.html')

def signup(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'signup.html',{'user_form':user_form,'registered':registered})

# def myexperience(request):
#     return render(request,'myexperience.html')

def myexperience(request):
    all_experience_items = ExperienceItem.objects.all()
    return render(request, 'myexperience.html',{'all_items': all_experience_items})

def add_experience(request):
    new_item = ExperienceItem(content = request.POST['content'],title = request.POST['title'],user = request.user.username,tag = request.POST['tag'])
    new_item.save()
    return HttpResponseRedirect('myexperience')

def like_main(request,experience_id):
    item_to_like  = ExperienceItem.objects.get(id=experience_id)
    new_like, created = Like.objects.get_or_create(user=request.user, experience_id = experience_id)
    if not created:
        new_like.delete()
        item_to_like.likes -= 1
        item_to_like.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        item_to_like.likes += 1
        item_to_like.save()
        return HttpResponseRedirect(reverse('index'))

def like_specific(request,experience_id):
    item_to_like  = ExperienceItem.objects.get(id=experience_id)

    new_like, created = Like.objects.get_or_create(user=request.user, experience_id = experience_id)
    if not created:
        new_like.delete()
        item_to_like.likes -= 1
        item_to_like.save()
        return render(request,'post_detail.html',{'experience':item_to_like})
    else:
        item_to_like.likes += 1
        item_to_like.save()
        return  render(request,'post_detail.html',{'experience':item_to_like})

def delete_experience(request, experience_id):
    item_to_delete = ExperienceItem.objects.get(id=experience_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('myexperience'))
