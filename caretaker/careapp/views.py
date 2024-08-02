from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from .models import Category,Surgicals
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from careapp.models import AdminProfile
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def login1(request):
    return render(request,'login.html')

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        
        if user is not None:
            with transaction.atomic():
                login(request, user)
                # Perform other operations as needed
            return redirect('admin_home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def admin_home(request):
    categories = Category.objects.all()
    return render(request, 'admin_home.html', {'categories': categories})



def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        if category_name:
            Category.objects.create(name=category_name)
            return redirect('add_surgical')  
    return render(request, 'add_surgical.html')

def logout1(request):
    logout(request)
    return redirect('index')

def surgical(request, group_name):
    surgical_items = Surgicals.objects.filter(group=group_name)
    context = {
        'surgical_items': surgical_items,
        'group_name': group_name,
        
    }
    return render(request, 'surgical.html', context)


def add_surgical(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        name = request.POST.get('name')
        image = request.FILES.get('image')
        
        surgical = Surgicals(group=group, name=name, image=image)
        surgical.save()
        
        return redirect('add_surgical')  # Redirect to a success page or the list of surgical items
    
    categories = Category.objects.all()
    return render(request, 'add_surgical.html', {'categories': categories})
   

def adminaddcategory(request):
    return render(request,'adminaddcategory.html')



def portfolio(request):
    return render(request,'portfolio.html')


from django.shortcuts import render, redirect
from .models import AdminProfile

from django.shortcuts import render, redirect
from .models import AdminProfile

def submit_admin_portfolio(request):
    if request.method == "POST":
        admin_name = request.POST.get("admin_name")
        admin_address = request.POST.get("admin_address")
        admin_email = request.POST.get("admin_email")
        admin_phone = request.POST.get("admin_phone")
        profile_picture = request.FILES.get("profile_picture")

        # Check if the email already exists
        if AdminProfile.objects.filter(email=admin_email).exists():
            return render(request, 'admin_profile_list.html', {"error_message": "This email is already associated with another profile."})

        admin_profile = AdminProfile(
            name=admin_name,
            address=admin_address,
            email=admin_email,
            phone=admin_phone,
            profile_picture=profile_picture
        )
        admin_profile.save()
        return redirect('admin_profile_list')

    return redirect('dmin_profile_list')



def viewportfolio(request):
    return render(request,'viewportfolio.html')


def admin_profile_list(request):
    profiles = AdminProfile.objects.all()
    return render(request, 'admin_profile_list.html', {'profiles': profiles})


def edit_admin_profile(request, pk):
    profile = get_object_or_404(AdminProfile, pk=pk)
    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.address = request.POST.get('address')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES.get('profile_picture')
        profile.save()
        return redirect('admin_profile_list')
    
    return render(request, 'edit_admin_profile.html', {'profile': profile})

def surgical_list(request):
    categories = Category.objects.all()
    return render(request, 'surgical_list.html', {'categories': categories})

def syringes(request):
    return render(request,'syringes.html')

def belts(request):
    return render(request,'belts.html')

def support(request):
    return render(request,'support.html')

def gloves(request):
    return render(request,'gloves.html')

def dressing(request):
    return render(request,'dressing.html')

def hotwaterbag(request):
    return render(request,'hotwaterbag.html')

def thermo(request):
    return render(request,'thermo.html')

def sthe(request):
    return render(request,'sthe.html')

def neb(request):
    return render(request,'neb.html')

def bp(request):
    return render(request,'bp.html')

def dipers(request):
    return render(request,'dipers.html')

def hyg(request):
    return render(request,'hyg.html')

def baby(request):
    return render(request,'baby.html')

def mask(request):
    return render(request,'mask.html')

def vapor(request):
    return render(request,'vapor.html')

def cot(request):
    return render(request,'cot.html')

def other(request):
    return render(request,'other.html')


def delete_admin_profile(request, pk):
    profile = get_object_or_404(AdminProfile, pk=pk)
    profile.delete()
    messages.success(request, 'Admin profile has been deleted successfully.')
    return redirect('admin_profile_list')


def your_view(request):
    surgical_items = Surgicals.objects.values_list('group', flat=True).distinct()
    return render(request, 'your_template.html', {'surgical_items': surgical_items})

@login_required
def delete_surgical(request, id):
    if request.method == 'DELETE':
        surgical_item = get_object_or_404(Surgicals, id=id)
        surgical_item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('admin_home') 