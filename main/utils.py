def extract_crsf(request):
    if('CSRF_COOKIE' in request.META and request.META['CSRF_COOKIE']):
        return request.META['CSRF_COOKIE']
    return None