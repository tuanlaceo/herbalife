from django.contrib import admin

# Register your models here.
from .models import Listing

# tao class de the hien nhung thong tin gi minh can biet trong admin
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)   # tao ra 1 list filter  dua tren ten cua realtor ben phai
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)