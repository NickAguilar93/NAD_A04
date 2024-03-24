from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.http import JsonResponse
# Create your views here.

def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                'bio': instance.bio,
                'avatar': instance.avatar.url,
                'user': instance.user.username
            })
            
    context = {
        'obj': obj,
        'form': form,
    }
        
        
    return render(request, 'profiles/main.html', context)

def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                'bio': instance.bio,
                'avatar': instance.avatar.url if instance.avatar else None,  # Check if avatar exists
                'user': instance.user.username
            })
        else:
            # In case form is not valid and it's an AJAX request, you might want to return errors
            return JsonResponse({'errors': form.errors}, status=400)
    
    # This part will handle non-AJAX requests or AJAX requests where the form is not valid
    context = {
        'obj': obj,
        'form': form,
    }
    
    return render(request, 'profiles/main.html', context)