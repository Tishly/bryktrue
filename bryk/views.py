from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import requests
from bs4 import BeautifulSoup as bs
from .models import Jobs_Listings

# Create your views here.
def index(request):

    if request.method == 'POST':
        job_title = request.POST['job_title']
        user = request.POST['user']
        url = 'https://www.myjobmag.com/search/jobs?q=software+engineering&field=ICT+%2F+Computer&industry=ICT+%2F+Telecommunication&experience=None'
        r = requests.get(url)
        soup = bs(r.content)
        profile = soup.find('h3', class_='left-section').text
        
        new_job = Jobs_Listings(
            job_title = job_title,
            imagelink = profile,
            username = user
        )
        new_job.save()
        messages.info(request, 'new '+ job_title +' job saved')
        return redirect('/')

    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def saved_jobs(request):
    username = request.user
    my_jobs = Jobs_Listings.objects.filter(username=username)
    return render(request, 'job.html', {'my_jobs':my_jobs})