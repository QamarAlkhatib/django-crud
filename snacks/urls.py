from django.urls import path
from .views import ListSnackView,DetailSnackView,DeleteSnackView,UpdateSnackView,CreateSnackView

urlpatterns = [
        path('',ListSnackView.as_view(), name = 'snack_list'),
        path('<int:pk>/', DetailSnackView.as_view(), name = 'snack_detail'),
        path('create/', CreateSnackView.as_view(), name = 'create_snack'),
        path('update/<int:pk>/', UpdateSnackView.as_view(), name = 'update_snack'),
        path('delete/<int:pk>/', DeleteSnackView.as_view(), name = 'delete_snack')
]
