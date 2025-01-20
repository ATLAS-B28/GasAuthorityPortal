from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import ServiceTrackRequests
from django.http import HttpResponse
from .forms import ServiceTrackRequestsForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_list_or_404

# Create your views here.

@login_required
def submit_req(request):
    if request.method == 'POST':
        form = ServiceTrackRequestsForm(request.POST, request.FILES)
        if form.is_valid():
            service_req = form.save(commit=False)
            service_req.customer = request.user
            service_req.save()
            return redirect('service_track_requests')
    else:
        form = ServiceTrackRequestsForm()
    return render(request, 'customer_service/submit_req.html', {'form': form})
    
@login_required
def service_track_requets(request):
    service_req = ServiceTrackRequests.objects.filter(customer=request.user).order_by('-created_at')

    return render(request, 'customer_service/service_track_requests.html', {'service_track_requests': service_req})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login_page')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('service_track_requests')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'navbar/login_page.html')

def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Are Registered Successfully")
            return redirect('login_page')
    else:
        form = SignUpForm()
        return render(request, 'customer_service/register_page.html', {'form': form})
    
    return render(request, 'customer_service/register_page.html', {'form': form})
    
def modify_req(request, req_id):
    service_req = get_object_or_404(ServiceTrackRequests, id=req_id, customer=request.user)

    if request.method == 'POST':
        form = ServiceTrackRequestsForm(request.POST, request.FILES, instance=service_req)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been updated Successfully")
            return redirect('service_track_requests')
    else:
        form = ServiceTrackRequestsForm(instance=service_req)
    
    return render(request, 'customer_service/modify_req.html', {'form': form, 'service_track_requests': service_req})


def delete_req(request, request_id):
    if request.user.is_authenticated:
        delete_it = ServiceTrackRequests.objects.get(id=request_id)
        delete_it.delete()
        messages.success(request, "Request Deleted Successfully..")
        return redirect('service_track_requests')
    else:
        messages.success(request, "You must be logged in to do that....")
        return redirect('login_page')