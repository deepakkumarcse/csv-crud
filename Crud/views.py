from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import csv
from . import models
from .forms import UserCreateForm


def main(request):
    form = UserCreateForm()
    return render(request, 'main.html', {'form': form, 'user_list': models.User.objects.all()})


def upload_csv(request):
    if request.method == "POST":
        data_list = csv.read_excel()
        for data in data_list:
            models.User.objects.get_or_create(name=data[0], email=data[1], phone=data[2])
        users = list(models.User.objects.values())
        return JsonResponse({'status': 200, 'message': 'Record(s) uploaded successfully', 'user_list': users})
    else:
        return JsonResponse({'status': 400, 'message': 'Something went wrong.'})


def save_data(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user_id = request.POST.get('user_id')
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            if user_id == '':
                user = models.User(name=name, email=email, phone=phone)
                message = 'New record added successfully.'
            else:
                user = models.User(id=user_id, name=name, email=email, phone=phone)
                message = 'Record Updated successfully.'
            user.save()
            users = list(models.User.objects.values())
            return JsonResponse({'status': 200, 'message': message, 'user_list': users})
        else:
            return JsonResponse({'status': 400, 'message': 'Something went wrong.'})


def delete_data(request):
    if request.method == "POST":
        uid = request.POST.get('user_id')
        try:
            user = models.User.objects.get(id=uid)
        except models.User.DoesNotExist:
            return JsonResponse({'status': 400, 'message': 'user does not exists.'})
        user.delete()
        return JsonResponse({'status': 200, 'message': 'user deleted successfully'})
    else:
        return JsonResponse({'status': 'Something went wrong.'})


def edit_data(request):
    if request.method == 'POST':
        uid = request.POST.get('user_id')
        try:
            user = models.User.objects.get(id=uid)
        except models.User.DoesNotExist:
            return JsonResponse({'status': 400, 'message': 'User does not exist.'})
        user_data = {'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone}
        return JsonResponse(user_data)
    else:
        return JsonResponse({'status': 400, 'message': 'Something went wrong.'})
