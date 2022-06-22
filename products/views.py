from functools import partial
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductModelSerializer
from .models import Product as ProductModel
from django.utils import timezone
from django.db.models.query_utils import Q


# Create your views here.
class ProductView(APIView):
    def get(self, request):
        today = timezone.now()
        products = ProductModel.objects.filter(
            Q(exposure_start_date__lte=today, exposure_end_date__gte=today, )| Q(user=request.user)
        )
        
        serializer_data = ProductModelSerializer(products, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        product_serializer = ProductModelSerializer(data=request.data)
        
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = ProductModel.objects.get(id=product_id)
        product_serializer = ProductModelSerializer(product, data=request.data, partial=True)
        
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        return Response({"delete method"})