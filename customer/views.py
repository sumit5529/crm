from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from chatapp import signals
from chatapp.models import ChatRoom
def customer_list(request):
    customers = Customer.objects.all()
    chatroom = ChatRoom.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers,'chatroom':chatroom})

@login_required 
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            useremail = form.cleaned_data['email']
            if Customer.objects.filter(name=username).count()==0 and Customer.objects.filter(email=useremail).count()==0:
                form.save()
                signals.notification.send(sender=Customer,request = request,username=username ,useremail = useremail)
            else:
                messages.success(request, 'This user already exist ')
                form = CustomerForm()
                return render(request, 'customer/add_customer.html', {'form': form})
             
             
             
            return redirect('customer:customer_list')  
    else:
        form = CustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})

@login_required 
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customer/edit_customer.html', {'form': form, 'customer': customer})

@login_required 
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:customer_list')
    return render(request, 'customer/delete_customer.html', {'customer': customer})
