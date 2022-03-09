from django.urls import path # nhap duong dan

from . import views  # . nghia la dang o trong cung folder pages

urlpatterns = [
    path('', views.index, name='index'), # trang dau tien se lay tai views def index()
                      #def index( duoc dat ten la index voi noi dung tuong ung tra ve  trog def index())
    path('about', views.about, name='about'),    # se chuyen den views chua def about va se dan toi about.html theo chuc nang trong def about
]
