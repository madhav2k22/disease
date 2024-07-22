# detector/views.py
import tensorflow as tf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from django.conf import settings
# from tensorflow.keras.models import load_model
from PIL import Image
import io
import os
import cv2
import numpy as np



class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['file']
            try:
                # Open and process the image
                image = Image.open(image)
                image = image.resize((150, 150))  
                # b,g,r = cv2.split(image)       # get b,g,r
                # rgb_img = cv2.merge([r,g,b])     # switch it to rgb
                # img_rank4 = np.expand_dims(rgb_img/255, axis=0)
                # label_map={'Pepper__bell___Bacterial_spot': 0, 'Pepper__bell___healthy': 1, 'Potato___Early_blight': 2, 'Potato___Late_blight': 3, 'Potato___healthy': 4, 'Tomato_Bacterial_spot': 5, 'Tomato_Early_blight': 6, 'Tomato_Late_blight': 7, 'Tomato_Leaf_Mold': 8, 'Tomato_Septoria_leaf_spot': 9, 'Tomato_Spider_mites_Two_spotted_spider_mite': 10, 'Tomato__Target_Spot': 11, 'Tomato__Tomato_YellowLeaf__Curl_Virus': 12, 'Tomato__Tomato_mosaic_virus': 13, 'Tomato_healthy': 14}

           
                # Example resizing
                # Return a successful response
                return Response({"message": "Image processed  and save successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                # Log the exception and return an error response
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
