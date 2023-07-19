from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin


class SaveIpAddressMiddleware(MiddlewareMixin):
    # Save the Ip address if does not exist
    def process_request(self, request):
        # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(',')[-1].strip()
        # else:
        #     ip = request.META.get('REMOTE_ADDR')
        # try:
        #     UserIP.objects.get(user_ip=ip)
        # except UserIP.DoesNotExist:
        #     ip_address = UserIP(user_ip=ip)
        #     ip_address.save()
        return None


class FilterIPMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        return None
