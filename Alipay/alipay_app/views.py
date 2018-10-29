from django.shortcuts import render, redirect
from Alipay import settings
from alipay import AliPay

# Create your views here.


def alipay(request):
    alipay = AliPay(
        appid="2016092100560320",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=settings.app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=settings.alipay_public_key_string,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False  # 默认False
    )

    subject = '请给我一千块'
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单编号
        out_trade_no="20181029sz1806",
        total_amount=1000,
        subject=subject ,
        return_url="http://1000phone.com",
        notify_url="https://example.com/notify"  # 可选, 不填则使用默认notify url
    )
    url = 'https://openapi.alipaydev.com/gateway.do?' + order_string

    return redirect(url)
