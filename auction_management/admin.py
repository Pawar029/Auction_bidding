from django.contrib import admin
from .models import Auction, Bid

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'start_time', 'end_time', 'start_price', 'winner')
    list_filter = ('start_time', 'end_time', 'winner')
    search_fields = ('item_name',)
    date_hierarchy = 'start_time'

class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction', 'bid_amount', 'timestamp')
    list_filter = ('user', 'auction')
    date_hierarchy = 'timestamp'

# Register the Auction and Bid models with the custom admin classes
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)

