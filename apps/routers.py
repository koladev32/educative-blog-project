from rest_framework import routers
from apps.authentication.viewsets import RegistrationViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegistrationViewSet, basename='auth-register')


urlpatterns = [
    *router.urls,
]