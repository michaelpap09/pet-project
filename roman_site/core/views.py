from django.shortcuts import render


def error404(request, exception):
    return render(request, 'core/404.html', status=404) 


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)