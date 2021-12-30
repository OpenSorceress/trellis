from django.http import Http404
from rest_framework.exceptions import APIException


def handle_exception(self, exc: Exception, action: str, request_id):
    """
    Handle any exception that occurs, by sending an appropriate message
    """
    # if isinstance(exc, APIException):
    #     self.reply(
    #         action=action,
    #         errors=self._format_errors(exc.detail),
    #         status=exc.status_code,
    #         request_id=request_id,
    #     )
    # elif exc == Http404 or isinstance(exc, Http404):
    #     self.reply(
    #         action=action,
    #         errors=self._format_errors("Not found"),
    #         status=404,
    #         request_id=request_id,
    #     )
    # else:
    #     raise exc
