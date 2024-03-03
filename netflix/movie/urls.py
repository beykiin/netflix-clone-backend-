from django.urls import path
from movie.views import *

urlpatterns = [
    path("browse-index/",browse_index,name="browse-index")
]
