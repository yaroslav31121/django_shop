from django.apps import AppConfig
from paypal.standard.ipn.models import PayPalIPN as BasePayPalIPN


class PaypalIpnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'paypal_IPN'

    def ready(self):
        import paypal.standard.ipn.signals
        paypal.standard.ipn.signals.valid_ipn_received.connect(PayPalIPN.ipn_valid)
        paypal.standard.ipn.signals.invalid_ipn_received.connect(PayPalIPN.ipn_invalid)



class PayPalIPN(BasePayPalIPN):

    ipn_valid = None
    ipn_invalid = None

    class Meta:
        app_label = 'paypal_IPN'



