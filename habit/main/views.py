from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Habit

# Create your views here.

def home(request):
  
  habits = Habit.objects.all()
  
  #Check to see if logging in 
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    #Authenticate
    if username is not None and password is not None:
     user = authenticate(request, username=username, password=password)
     if user is not None:
      login(request,user)
      messages.success(request, 'You have been logged in')
      return redirect('home')
     else:
      messages.success(request,"There was an error logging in, please try again")
      return redirect('home')
    return redirect('home')
  else:
   return render(request, 'home.html', {'habits':habits})

def logout_user(request):
  logout(request)
  messages.success(request, 'You have been logged out ')
  return redirect('home')

def register_user(request):
  
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      #user authentication
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username,pasword=password)
      login(request,user)
      messages.success(request,'You have sucessfully registered, welcome')
      return redirect('home')
  else:
    form=SignUpForm() 
  return render(request, 'register.html', {'form':form})

def habit_record(request,pk):
  if request.user.is_authenticated:
    #look up records
    habit_record = Habit.objects.get(id=pk)
    return render(request, 'record.html', {'habit_record':habit_record})
  else:
    messages.success(request,'You must be logged in to view the page')
    return redirect('home')

def delete_habit(request,pk):
  if request.user.is_authenticated:
    delete_records = Habit.objects.get(id=pk)
    delete_records.delete()
    messages.success(request,'Habit deleted successfully!')
    return redirect('home')
  else:
    messages.success(request,'You must login to delete the habit!')
    return redirect('home')

def add_habit(request):
    form = AddRecordForm(request.POST or None)  # Create the form

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_habit = form.save(commit=False)  # Don't commit yet
                add_habit.user = request.user  # Assign current user
                add_habit.save()  # Save the form data with assigned user

                messages.success(request, "Record Added Successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})  # Render form on GET
    else:
        messages.error(request, "You Must Be Logged In...")  # Use "error" for login requirement
        return redirect('home')
      
def update_habit(request,pk):
  if request.user.is_authenticated:
    current_habit = Habit.objects.get(id=pk)
    if request.method=='POST':
      form = AddRecordForm(request.POST or None, instance=current_habit)
      if form.is_valid():
        form.save()
        messages.success(request, 'Habit has been updated')
        return redirect('home')
    else:  
      form = AddRecordForm( instance=current_habit)
    return render(request, 'update_record.html',{'form':form})  
  else:
    messages.success(request, 'You must be logged in...')
    return redirect('home')