# auctionmanagement/urls.py
from django.urls import path
from .views import AuctionList, AuctionDetail, BidList, BidDetail

urlpatterns = [
    path('auctions/', AuctionList.as_view(), name='auction-list'),
    path('auctions/<int:pk>/', AuctionDetail.as_view(), name='auction-detail'),
    path('bids/', BidList.as_view(), name='bid-list'),
    path('bids/<int:pk>/', BidDetail.as_view(), name='bid-detail'),
]
