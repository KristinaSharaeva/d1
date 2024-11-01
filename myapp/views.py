from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = """
    <html>
    <body>
        <h1>Добро пожаловать на мой первый сайт Django!</h1>
        <p>Это главная страница моего сайта.</p>
    </body>
    </html>
    """
    logger.info(f"Главная страница посещена с IP: {request.META['REMOTE_ADDR']}")
    return HttpResponse(html)

def about(request):
    html = """
    <html>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Я начинающий разработчик и это мой первый сайт на Django.</p>
    </body>
    </html>
    """
    logger.info(f"Страница 'О себе' посещена с IP: {request.META['REMOTE_ADDR']}")
    return HttpResponse(html)
