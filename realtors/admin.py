from django.contrib import admin   

# Register your models here.
from .models import Realtor   # dang ki trong admin thi se hien Realtor trong phan admin de cap nhat


class RealtorAdmin(admin.ModelAdmin):   #tao class nay ke thua Model admin cua Realtor ma ta import vao ben tren
  list_display = ('id', 'name', 'email', 'hire_date','is_mvp')
  list_editable = ('is_mvp',)    # them tinh nang tick co fai la mvp ngay giao dien ben ngoai luon: danh cho True /False thoi
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
