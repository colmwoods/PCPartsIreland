from django.conf import settings
from django.http import HttpResponsePermanentRedirect

class CanonicalDomainMiddleware:
    """
    Redirects any non-canonical host (including *.herokuapp.com and the apex)
    to the canonical domain (e.g. www.pcpartsireland.com).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Don't interfere with local development
        if settings.DEBUG:
            return self.get_response(request)

        canonical_host = getattr(settings, "CANONICAL_HOST", None)
        if not canonical_host:
            return self.get_response(request)

        host = request.get_host().split(":")[0]

        # Redirect herokuapp.com and apex to canonical
        if host.endswith("herokuapp.com") or host == "pcpartsireland.com":
            return HttpResponsePermanentRedirect(
                f"https://{canonical_host}{request.get_full_path()}"
            )

        return self.get_response(request)
