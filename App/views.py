from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserImageForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate,login,logout
from .models import UserImageModel
import numpy as np
from tensorflow import keras
from PIL import Image,ImageOps

# import pyttsx3
# import time


def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

from .models import Profile

def profile(request):
    user = request.user
    # Ensure the user has a profile
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

from . models import UserImageModel
from . import forms
from .forms import UserImageForm


def Deploy_8(request): 
    print("HI")
    if request.method == "POST":
        form = forms.UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserImageModel.objects.latest('id')
        models = keras.models.load_model('App/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ["AFFECTED_PCOS","infected_PCOD","NORMAL_PCOS","notinfected_PCOD"]
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == "AFFECTED_PCOS":
            b ='This Image Detected AFFECTED_PCOS'
        elif a == "infected_PCOD":
            b ='This Image Detected infected_PCOD'
        elif a == "NORMAL_PCOS":
            b ='This Image Detected NORMAL_PCOS'
        elif a == "notinfected_PCOD":
            b ='This Image Detected notinfected_PCOD'
        
       

        else:
            b = 'WRONG INPUT'

        data = UserImageModel.objects.latest('id')
        data.label = a
        data.save()

        # engine = pyttsx3.init()
        # rate = engine.getProperty('rate')
        # engine.setProperty('rate', rate - 10)  # Decrease rate by 50 (default rate is typically around 200)
        # engine.say(a)
        # engine.runAndWait()

        
        # text_to_speech(a, delay=7)

        
        return render(request, 'App/output.html',{'form':form,'obj':obj,'predict':a, 'predicted':b})
    else:
        
        form = forms.UserImageForm()
    return render(request, 'App/model.html',{'form':form})

import joblib

Model = joblib.load('App/PCOS1.pkl')
import numpy as np
from django.shortcuts import render
from .forms import HealthAssessmentForm
from .models import HealthAssessment

def Deploy_9(request):
    form = HealthAssessmentForm()  # Initialize the form outside the if block
    
    if request.method == 'POST':
        form = HealthAssessmentForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Age = cleaned_data['Age']
            Weight = cleaned_data['Weight']
            Height = cleaned_data['Height']
            BMI = cleaned_data['BMI']
            Blood_Group = cleaned_data['Blood_Group']
            Pulse_rate = cleaned_data['Pulse_rate']
            RR = cleaned_data['RR']
            Hb = cleaned_data['Hb']
            Marriage_Status = cleaned_data['Marriage_Status']
            Pregnant = cleaned_data['Pregnant']
            No_of_abortions = cleaned_data['No_of_abortions']
            TSH = cleaned_data['TSH']
            PRG = cleaned_data['PRG']
            RBS = cleaned_data['RBS']
            Weight_gain = cleaned_data['Weight_gain']
            Hair_loss = cleaned_data['Hair_loss']
            Fast_food = cleaned_data['Fast_food']
            Reg_Exercise = cleaned_data['Reg_Exercise']
            BP_Systolic = cleaned_data['BP_Systolic']
            BP_Diastolic = cleaned_data['BP_Diastolic']
            Follicle_No_L = cleaned_data['Follicle_No_L']
            Follicle_No_R = cleaned_data['Follicle_No_R']
            
            # Create a feature array for prediction
            feature = np.array([[
                Age, Weight, Height, BMI, Blood_Group, Pulse_rate, RR, Hb, Marriage_Status, Pregnant, No_of_abortions, TSH, PRG, RBS, Weight_gain, Hair_loss, Fast_food, Reg_Exercise, BP_Systolic, BP_Diastolic, Follicle_No_L, Follicle_No_R
            ]])
            
            predictions = Model.predict(feature)  # Call predict on your model instance

            output = predictions[0] 
            
            if output == 0:
                result = "YES_PCOS_FOUND"
            elif output == 1:
                result = "NO_PCOS_NOT_FOUND"
            
            # Save the form data and result
            instance = form.save(commit=False)
            instance.PCOS = result
            instance.save()
            
            return render(request, 'app/ml_output.html', {"prediction_text": result})
        else:
            print('Form is not valid')
        
    return render(request, 'app/9_deploy.html', {"form": form})


def ML_DB(request):
    predictions = HealthAssessment.objects.all()
    return render(request, 'App/ML_DB.html', {'predictions':predictions })

def Basic(request):
    return render(request,'App/Basic_report.html')

def Metrics(request):
    return render(request,'App/Metrics_report.html')

def Database(request):
    models = UserImageModel.objects.all()
    return render(request, 'App/Database.html', {'models': models})

from .models import Profile

def profile_list(request):
    # Fetch all profile objects from the database
    profiles = Profile.objects.all()
    
    # Pass the profiles data to the template
    return render(request, 'app/profile_list.html', {'profiles': profiles})



def logout_view(request):  
    auth_logout(request)
    return redirect('/')