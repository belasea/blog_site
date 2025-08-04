from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notification
from django.contrib import messages


def notification_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        queryset = Notification.objects.filter(user=request.user).order_by('-id')
        query = request.GET.get('q')
        if query:
            # Using strip method to remove extra white space
            query = query.strip()
            queryset = Notification.objects.filter(
                Q(message__icontains=query) |
                Q(message__istartswith=query) |
                Q(message__endswith=query) |
                Q(user__email__icontains=query)
            ).distinct()
        page = request.GET.get('page')
        paginator = Paginator(queryset, 7)  # 10 posts per page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'object_list': posts,
            'page': page
        }
        return render(request, 'notification/notification.html', context)
    else:
        messages.add_message(request, messages.WARNING, "Sorry you don't have access this file")
        return redirect('home')
    

def read_notification(request, pk):
    notification = get_object_or_404(Notification, id=pk)

    # Optional: Ensure only owner or superuser can mark it read
    if request.user == notification.user or request.user.is_superuser:
        notification.read = True
        notification.save()

        # Redirect to the actual link
        if notification.link:
            return redirect(notification.link)
    return redirect('notification') 



def delete_notification(request, id):
    obj = get_object_or_404(Notification, pk=id)
    obj.delete()
    messages.add_message(request, messages.WARNING, "Successfully delete notification !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
