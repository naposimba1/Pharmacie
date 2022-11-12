from django.urls import include,  path
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()

router.register("Province", ProvinceViewSet)
router.register("Commune", CommuneViewSet)
router.register("Zone", ZoneViewSet)
router.register("Quartier", QuartierViewSet)
router.register("Agence", AgenceViewSet)
router.register("Personnel", PersonnelViewSet)
router.register("Stock", StockViewSet)
router.register("Vente", VenteViewSet)
router.register("Client", ClientViewSet)
router.register("Dette", DetteViewSet)
router.register("Mutuelle", MutuelleViewSet) 
router.register("Produit", ProduitViewSet)


urlpatterns=[
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urlsrouter.register(Province, ProvinceViewSet)
]