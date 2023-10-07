from django.shortcuts import render

# Create your views here.
# auctionmanagement/views.py
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Auction
from .serializers import AuctionSerializer

from rest_framework.permissions import IsAuthenticated
from .models import Bid
from .serializers import BidSerializer

class AuctionList(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAdminUser]  # Only admin can list and create auctions

class AuctionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAdminUser]  # Only admin can view, update, and delete auctions


class BidList(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can list and create bids

    def perform_create(self, serializer):
        # Automatically set the user making the bid
        serializer.save(user=self.request.user)

class BidDetail(generics.RetrieveAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
