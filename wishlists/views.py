from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Wishlist
from .serializers import WishlistSerializer


class Wishlists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(
            all_wishlists, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            new_wishlist = serializer.save(user=request.user)
            return Response(WishlistSerializer(new_wishlist).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
