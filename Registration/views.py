from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import RegistrationForm
from .models import Registration, Session
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'Registration/index.html')

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'Registration/registration.html', {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect('/successful-submission/')
        return render(request, 'Registration/registration.html', {"form": form})
        
class SuccesfulSubmissionView(View):
    def get(self, request):
        return render(request, 'Registration/successful.html')

class ParticipantsView(View):
    def get(self, request):
        participants = Registration.objects.all()
        return render(request, 'Registration/participants.html', {'participants': participants})
    
class EditView(View):
    def get(self, request, pk):
        registration = Registration.objects.get(pk=pk)
        form = RegistrationForm(instance=registration)
        return render(request, 'Registration/edit.html', {'form': form, 'registration': registration})
    
    def post(self, request, pk):
        registration = Registration.objects.get(pk=pk)
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/participants/')
        return render(request, 'Registration/edit.html', {'form': form, 'registration': registration})

class DeleteView(View):
    def get(self, request, pk):
        registration = Registration.objects.get(pk=pk)
        return render(request, 'Registration/delete.html', {'registration': registration})
    
    def post(self, request, pk):
        registration = Registration.objects.get(pk=pk)
        registration.delete()
        return HttpResponseRedirect('/participants')