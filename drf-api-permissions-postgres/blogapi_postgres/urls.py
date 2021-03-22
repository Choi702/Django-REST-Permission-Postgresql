from django.urls import path
from .views import blogapi_postgresList, blogapi_postgresDetail

urlpatterns = [
    path('', blogapi_postgresList.as_view(), name='blogapi_postgres_list'),
    path('<int:pk>/', blogapi_postgresDetail.as_view(), name='blogapi_postgres_detail')
]