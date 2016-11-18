from rest_framework import routers

from time_tracking.api import ProjectViewSet, EntryViewSet

api_router = routers.SimpleRouter()
api_router.register(r'projects', ProjectViewSet)
api_router.register(r'entries', EntryViewSet)

