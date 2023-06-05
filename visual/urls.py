from django.urls import path
from .views import ApplicationProducersDetailView, AddBookView

urlpatterns = [
    path('', AddBookView.as_view(), name='home'),
    path('<int:apl_id>/', ApplicationProducersDetailView.as_view(), name='details'),
]
