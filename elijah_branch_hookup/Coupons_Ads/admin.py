from django.contrib import admin
from Coupons_Ads.models import Coupon, Ad
# Register your models here.


class CouponAdmin(admin.ModelAdmin):
    pass

class AdAdmin(admin.ModelAdmin):
    pass


admin.site.register(Coupon, CouponAdmin)
admin.site.register(Ad, AdAdmin)

