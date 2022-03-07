from rest_framework import routers
from apps.authentication.viewsets import RegistrationViewSet, LoginViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')


urlpatterns = [
    *router.urls,
]