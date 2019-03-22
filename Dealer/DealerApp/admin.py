from django.contrib import admin
from DealerApp.models import BikePurchase,PostEnquiry,BikeSale
# Register your models here.

class PostEnquiryAdmin(admin.ModelAdmin):
    list_display=['Name','Vehicle','BIKE_Model','Color','Contact_Number']

admin.site.register(PostEnquiry,PostEnquiryAdmin)
