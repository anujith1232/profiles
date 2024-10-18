from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import Paginator, EmptyPage


def profile_details(request):
    profiles = Profile.objects.all()  # Query all profile instances

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)  # Use request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('profile_details')  # Redirect to the same page after saving
    else:
        form = ProfileForm()

    return render(request, 'profile_details.html', {'form': form, 'profiles': profiles})

def overview(request, profile_id):
    profiles = Profile.objects.get(id=profile_id)  # Get the profile using get()
    return render(request, 'overview.html', {'profiles': profiles})

def datas(request):
    profiles = Profile.objects.all()
    return render(request, 'datas.html', {'profiles': profiles})

def deleteview(request, profile_id):
    profiles = Profile.objects.get(id=profile_id)
    if request.method == "POST":
        profiles.delete()
        return redirect("profile_details")
    return render(request, 'deleteview.html', {'profiles': profiles})

def updateview(request, profile_id):
    profiles = Profile.objects.get(id=profile_id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profiles)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("datas")

    return render(request, 'updation.html', {'form': form, 'profiles': profiles})

def search(request):
    query = None
    profiles = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        profiles = Profile.objects.filter(Q(username__icontains=query))
    else:
        profiles = []

    context = {'profiles': profiles, 'query': query}
    return render(request, 'search.html', context)

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Homepage')
        else:
            messages.info(request, 'Please provide correct details')
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return redirect('login')


def Homepage(request):

    return render(request,'home.html')

def totalview(request):
    profiles = Profile.objects.all()
    paginator = Paginator(profiles, 1)  # Show 6 profiles per page

    page_number = request.GET.get('page')  # Get the current page number from the URL
    try:
     page = paginator.get_page(page_number)
    except EmptyPage:
     Page=paginator.page(page_number.num_page)


    return render(request, 'profilesview.html', {'profiles':profiles,'page': page})




