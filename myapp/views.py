from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def myapphome(request):
	return render(request,'myapp/myapphome.html')


def signin(request):
	if request.user.is_authenticated:
		messages.success(request,'already logged in')
		return render(request,'myapp/myapphome.html')
	if request.method == 'POST':
		# import pdb;pdb.set_trace()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,'You are successfully logged in')
			return redirect('myapp:home')
		else:
			messages.error(request,'User Id not matched')
			form = AuthenticationForm(request.POST)
			return render(request,'myapp/login.html',{'form':form})
	else:
		form = AuthenticationForm()
		return render(request,'myapp/login.html',{'form':form})


def signup(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			# import pdb;pdb.set_trace()
			user.profile.genre = form.cleaned_data.get('genre')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.merritual_staus = form.cleaned_data.get('merritual_staus')
			user.save()
			messages.success(request,"Successfully registered with us, plz signin now")
			return redirect('myapp:login')
	else:
		form = SignUpForm()
		# import pdb;pdb.set_trace()
	return render(request,'myapp/signup.html',{'form':form})




def signout(request):
	logout(request)
	return redirect('myapp:login')