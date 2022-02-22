from django.urls import path
from AppReviews.views import ProductDescription, ProductReviewPage, ProductViewSetAPI


urlpatterns=[
    path('',ProductReviewPage.as_view()),
    path('products/',ProductViewSetAPI.as_view()),
    path('products/<int:pk>/',ProductDescription.as_view())
]
