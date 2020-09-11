from django.views.generic import View
from django.http import HttpResponse


class Home(View):
    """
    Class Based Generic View for dashboard page.
    This class based view will render the details for dashboard.
    This class overrides a generic method called get.
    """

    def get(self, request):
        """
        This method will render the data for dashboard.
        :param request: Object, Required, Contains data from GET or POST
        :return: Renders template with context data
        """
        return HttpResponse('This is a demo page!')

