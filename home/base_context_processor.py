from home.models import Header, Footer

def base_renderer(request):
    return {
        'header': Header.objects.order_by('-timestamp').first(),
        'footer': Footer.objects.order_by('-timestamp').first()
    }
