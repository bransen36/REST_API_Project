from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

class CustomRouter(DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        original_view = super().get_api_root_view(api_urls)

        def custom_root_view(request, *args, **kwargs):
            response = original_view(request, *args, **kwargs)
            if isinstance(response, Response):
                response.data['register'] = reverse('register', request=request)
            return response
        
        return custom_root_view