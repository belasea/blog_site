from home.models import Footer

def base_renderer(request):
    return {
       'footer': Footer.objects.all()[:1]
    }