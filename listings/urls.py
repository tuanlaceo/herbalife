from django.urls import path # nhap duong dan

from . import views  # . nghia la dang o trong cung folder pages

urlpatterns = [
    path('', views.index, name='listings'), # trang dau tien se lay tai views def index()
                      #def index( duoc dat ten la index voi noi dung tuong ung tra ve  trog def index())
    path('<int:listing_id>', views.listing, name='listing'),    # se chuyen den views chua def about va se dan toi about.html theo chuc nang trong def about
    path('search', views.search, name='search'), 
]
