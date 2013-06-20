from django.views.generic import TemplateView

from braces.views import JSONResponseMixin, AjaxResponseMixin

class MainPage(TemplateView):
    template_name = "marketing/home.html"

class ESLReceipt(JSONResponseMixin, AjaxResponseMixin, TemplateView):
    template_name = "esl_receipt/response.html"
    content_type = "text/html" # this needs to be conditional on the request method