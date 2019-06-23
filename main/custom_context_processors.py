from main.models import Page, ImageContent


def base_context(request):
    logo = ImageContent.objects.get(name="logo_1")
    page_list = Page.objects.all().order_by("order")
    active_app = request.resolver_match.app_names

    return {
        'logo': logo,
        'pages': page_list,
        'active_app': active_app[-1],
    }
