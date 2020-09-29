from rest_framework.throttling import SimpleRateThrottle


class AuthThrottle(SimpleRateThrottle):
    # rate = '10/m'
    scope = 'auth'
    def get_cache_key(self, request, view):
        return self.get_ident(request)