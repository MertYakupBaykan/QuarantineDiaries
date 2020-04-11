from django.shortcuts import render
from share_experience_app.forms import UserForm
from .models import ExperienceItem
#login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

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
    new_item = ExperienceItem(content = request.POST['content'],title = request.POST['title'],user = request.user.username)
    new_item.save()
    return HttpResponseRedirect('myexperience')

def delete_experience(request, experience_id):
    item_to_delete = ExperienceItem.objects.get(id=experience_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('myexperience'))
