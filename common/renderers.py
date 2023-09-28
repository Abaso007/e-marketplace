from rest_framework.renderers import JSONRenderer
import json
from django.core.serializers.json import DjangoJSONEncoder

class CustomRenderer(JSONRenderer):
    '''
    Ensure all API endpoints are rendered in the same format as in
    {
        'status': ....,
        'data': [...]
    }
    '''
    
    charset = "utf-8"
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ""

        return (
            json.dumps(
                {
                    "status": "Error",
                    "data": data,
                }
            )
            if "ErrorDetail" in str(data)
            else json.dumps(
                {
                    "status": "Successful",
                    "data": data,
                },
                cls=DjangoJSONEncoder,
            )
        )