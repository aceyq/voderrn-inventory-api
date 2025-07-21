from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response #allows status codes
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 #404 status code

from .models import Product, User
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

    #query gets all products from the database 
    #serializer uses serializer to format into JSON

class ProductCreateView(APIView):
    def post(self, request):
        seller_id = request.data.get('seller')  # changed from 'seller_id' to 'seller'
        seller = get_object_or_404(User, pk=seller_id)

        if seller.user_type != "seller":
            return Response({"error": "Only sellers can create products."}, status=403)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

        #uses serializer to validate and save the product to database
        #if valid, returns new product info, otherwise, sends back errors

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "product_id"

    #lets someone get a single product by its ID (UUID)
    #uses RetrieveAPIView which automatically handles the GET request

class ProductUpdateView(APIView):
    def put(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if product.seller.user_id != request.data.get("seller_id"):
            return Response({"error": "You can only update your own product."}, status=403)

#it checks: is the person trying to update this the seller who owns it?
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

#If everything’s valid, the product is updated and returned in the response.

class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        seller_id = request.query_params.get("seller_id")
        seller_id = request.query_params.get("seller_id")
        if not seller_id:
            return Response({"error": "Missing seller_id query parameter."}, status=400)

        try:
            seller_id = int(seller_id)
        except ValueError:
            return Response({"error": "seller_id must be an integer."}, status=400)

        user = get_object_or_404(User, pk=seller_id)

        if user.user_type != "admin" and product.seller.user_id != seller_id:
            return Response({"error": "Only the seller or an admin can delete this product."}, status=403)
        product.delete()
        return Response(status=204)
#find product + user trying to delete it
#only admin/seller can delete it
#if authorized, it deletes product + returns a 204 (NO CONTENT) status

class DeleteUserView(APIView):
    def delete(self, request, user_id):
        # Who is trying to delete this user?
        requester_id = request.data.get("requester_id")
        requester = get_object_or_404(User, pk=requester_id)

        # Only admins can delete users (not themselves)
        if requester.user_type != "admin":
            return Response({"error": "Only an admin can delete users."}, status=403)
        if requester_id == user_id:
            return Response({"error": "Admins cannot delete themselves."}, status=403)

        # Who is being deleted?
        user_to_delete = get_object_or_404(User, pk=user_id)

        # If the user is a seller, delete their products first
        if user_to_delete.user_type == "seller":
            Product.objects.filter(seller=user_to_delete).delete()

        user_to_delete.delete()
        return Response({"message": "User deleted successfully."}, status=204)

