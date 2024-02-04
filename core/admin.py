from django.contrib import admin
from django.db.models.aggregates import Count
from . import models

# Register your models here.

def make_refund_accepted(modeladmin,request, queryset):
    queryset.update(refund_requested=False,refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

    # def get_queryset(self, request):
    #     return super().get_queryset(request).annotate(
    #         orders_count=Count('order')
    #     )



    

    


admin.site.register(models.Product)
admin.site.register(models.OrderItem)
# admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Payment)
admin.site.register(models.Coupon)
admin.site.register(models.Refund)
# admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.UserProfile)