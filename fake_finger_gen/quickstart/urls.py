from django.urls import path
from .views import FakeFingerprintAPIView

urlpatterns = [path("fakeprint", FakeFingerprintAPIView.as_view())]
