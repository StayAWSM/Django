import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.debug('request: "index"')
    html = '<h1>Main page</h1>' \
           '<h2>My Django project!</h2>' \
           '<h4>Click to get info <a href="http://127.0.0.1:8000/about/">About us</a></h4>'
    return HttpResponse(html)


def about(request):
    logger.debug('request: "about"')
    html = '<h1>About us:</h1>' \
           '<h2>My name is Alexandr Babichev</h2>' \
           '<h3>I study Django for this project</h3>' \
           '<h4>Click to get to the <a href="http://127.0.0.1:8000/">Main page</a></h4>'
    return HttpResponse(html)
