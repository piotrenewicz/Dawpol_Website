from main.models import Page#, ImageContent


def base_context(request):
    page_list = Page.objects.all().order_by("order")
    active_app = request.resolver_match.app_names

    return {
        'pages': page_list,
        'active_app': active_app[-1],
    }
