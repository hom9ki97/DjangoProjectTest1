import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        logger.info(f'Запрос: {request.method} {request.path}')
        try:
            response = view_func(request, *args, **kwargs)
            logger.info(f'Ответ: {response.status_code}')
            return response
        except Exception as e:
            logger.error(f"Ошибка обработки запроса: {str(e)}")
            raise
    return wrapper