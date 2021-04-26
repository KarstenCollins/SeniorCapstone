from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import BankCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from .models import Bank




#def BankCreateView(request):
    #if request.method == 'Post':
        #form = BankCreateForm(request.POST)
        #if form.is_valid():
       #     form.save()
      #      messages.success(request, f'Your bank has been submitted!')
     #       return redirect('BankInfo/')
    #else:
     #   form = BankCreateForm()
    #return render(request, 'BankInformation/bank_form.html', {'form' : form})



class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    fields = ['bank_name', 'bank_acc_number', 'nickname', 'account_type', 'routing_number', 'notes']
    context_object_name = 'banks'

    def form_valid(self, form):
        form.instance.user = self.request.user #sets author to logged in user
        return super().form_valid(form)

class BankListView(LoginRequiredMixin, ListView):
    model = Bank
    template_name = 'BankInformation/bank_display.html'
    context_object_name = 'banks'

    def get_queryset(self): #only show logged in users' data
        return self.model.objects.all().filter(user=self.request.user)