from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
import json
from .serializer import *
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
class ProductByCategoryView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    def retrieve(self, request, *args, **kwargs):
        category_id=kwargs['pk']
        products=self.queryset.filter(category_id=category_id)
        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)
class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
class OrderDetailsView(viewsets.ModelViewSet):
    queryset = Order_details.objects.all()
    serializer_class = OrderDetailsSerializer
class OrderDetailsByOrdersView(viewsets.ModelViewSet):
    queryset = Order_details.objects.all()
    serializer_class = OrderDetailsSerializer
    def retrieve(self, request, *args, **kwargs):
        order_id=kwargs['pk']
        order_details=self.queryset.filter(order_id=order_id)
        serializers=self.get_serializer(order_details, many=True)
        return Response(serializers.data)
class OrderDetailsActionsView(viewsets.ModelViewSet):
    queryset = Order_details.objects.all()
    serializer_class = OrderDetailsSerializer

    def update(self, request, *args, **kwargs):  #put zoprosda keladi, shuning uchun update ga berib ketamiz
        od_id=kwargs['pk']
        #kelgan datani o'qib olishimiz kk
        data=json.loads(request.body)
        order_detail=self.queryset.get(id=od_id)
        order_detail.action(data)
        # print(request.body)
        return Response({'quantity':order_detail.quantity})

# Create your views here.
