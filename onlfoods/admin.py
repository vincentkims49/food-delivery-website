from django.contrib import admin
from .models import Customer, Region_manager,Region, Orders, Food, Feedback, Offers, monthly_plan


@admin.action(description='approve orders for delivery')
def approve_delivery(modeladmin, request, queryset):
    queryset.update(status='Delivery in progress')

class CustomerAdmin(admin.ModelAdmin):
    cust = Customer.objects.all().count()
    # cust = str(cust)
    list_display = ['user','c_email', 'c_phone_number','address','c_region']
admin.site.register(Customer, CustomerAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ['f_name','f_price', 'f_desc']
admin.site.register(Food, FoodAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered','expected_time','food','status']
    actions=[approve_delivery]
admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'date','feed']
admin.site.register(Feedback, FeedbackAdmin)

class OffersAdmin(admin.ModelAdmin):
    list_display = ['food', 'region','offer_expiry','percentage']
admin.site.register(Offers, OffersAdmin)

class RegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Region, RegionAdmin)

class Region_managerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Region_manager, Region_managerAdmin)

class montly_planAdmin(admin.ModelAdmin):
    list_display = ['food', 'customer','delivery_time']
    actions=[approve_delivery]
admin.site.register(monthly_plan,montly_planAdmin)