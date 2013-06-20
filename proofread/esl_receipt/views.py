from django.views.generic import TemplateView, View

from braces.views import JSONResponseMixin, AjaxResponseMixin


class ESLReceipt(TemplateView):
    template_name = "esl_receipt/response.html"

    def get(self, request, *args, **kwargs):
        context = {'response': 'You must POST a message'}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {'response': 'Success!'}
        return self.render_to_response(context)


class ESLReceiptAPI(JSONResponseMixin, AjaxResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'success': 0, 'message': 'You must POST a message'}
        return self.render_json_response(context)

    def post(self, request, *args, **kwargs):
        context = {'success': 1, 'message': "We got it!  You'll hear back soon"}
        return self.render_json_response(context)