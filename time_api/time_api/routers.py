from rest_framework import routers

from time_tracking.api import ProjectViewSet, EntryViewSet, TaskViewSet, ProfileViewSet, UserViewSet

api_router = routers.SimpleRouter()
api_router.register(r'projects', ProjectViewSet)
api_router.register(r'entries', EntryViewSet)
api_router.register(r'tasks', TaskViewSet)
api_router.register(r'profiles', ProfileViewSet)
api_router.register(r'users', UserViewSet)
