from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.views import generic 
from .models import User
from .forms import SignUpForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


#LIST OF ALL PRODUCT
class SignUpView(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup_form.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ask_questions:question_list')


def LogOut(request):
    logout(request)
    return redirect('ask_questions:question_list')

def LogIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try :
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('ask_questions:question_list' )
                else:
                    messages.error(request, "Invalid username or password.")
                    
            except :
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
        return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        return render( request,
                    "login.html",
                    {"form":form})
    
       
def SellerView(request):
    return render(request,'sellerView.html',)


