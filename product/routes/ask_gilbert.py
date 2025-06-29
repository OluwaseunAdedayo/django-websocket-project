from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from components.gilbert import gilbert
import json

class ask_gilbert(APIView):
    def post(self, request):
        request_data = request.data  

        if "seo_data" not in request_data:
            return Response({"error":True,"message":"Seo analysis is required"},status=status.HTTP_400_BAD_REQUEST)
        
        seo_data = json.dumps(request_data["seo_data"])
        prompt_number = request_data.get("prompt_number", 0)
        model_number = request_data.get("model_number", 0)

        inference_result = gilbert(seo_data,prompt_number,model_number)

        return Response({"error":False,'data': inference_result}, status=status.HTTP_200_OK)
