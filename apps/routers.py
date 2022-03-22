from rest_framework_nested import routers
from apps.authentication.viewsets import RegistrationViewSet, LoginViewSet
from apps.article.viewsets import ArticleViewSet
from apps.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')

# ##################################################################### #
# ################### ARTICLE                    ###################### #
# ##################################################################### #

router.register(r'article', ArticleViewSet, basename='article')

# ##################################################################### #
# ################### COMMENT                    ###################### #
# ##################################################################### #

article_router = routers.NestedSimpleRouter(router, r'article', lookup='article')
article_router.register(r'comment', CommentViewSet, basename='article-comment')

urlpatterns = [
    *router.urls,
    *article_router.urls
]