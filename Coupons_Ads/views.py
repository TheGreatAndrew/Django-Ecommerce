from django.shortcuts import render
from Coupons_Ads.models import Coupon, Ad
# Create your views here.

def Coupons_Ads_index(request):
    coupons = Coupon.objects.all()
    ads = Ad.objects.all()

    context = {
            'coupons': coupons,
            'ads': ads
    }

    return render(request, 'Coupons_Ads_index.html', context)


