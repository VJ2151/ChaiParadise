from django.shortcuts import render, get_object_or_404, redirect
from .models import ChaiVariety

# All Chai Page
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

# Orders Page
def orders(request):
    return render(request, 'chai/orders.html')

# Chai Detail Page
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

# Order Chai Page
def order_chai(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    
    # Placeholder logic (you can extend this to store orders in the database)
    order_message = f"You have successfully ordered {chai.name} for ₹{chai.price}!"
    
    return render(request, 'chai/order_success.html', {'chai': chai, 'order_message': order_message})
