from rest_framework.routers import DefaultRouter

from api.views import LocationViewSet, LitterViewSet, RatViewSet, PersonViewSet, PrefixViewSet

app_name = "api"

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'litters', LitterViewSet, basename='litters')
router.register(r'rats', RatViewSet, basename='rats')
router.register(r'prefix', PrefixViewSet, basename='prefix')
urlpatterns = router.urls
