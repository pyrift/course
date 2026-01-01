from django.contrib import admin
from  .models import *

admin.site.register(Branch)
admin.site.register(Burning)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name']

@admin.register(Infaration)
class InfarationAdmin(admin.ModelAdmin):
    list_display = ['young', 'phone_number', 'telegram_urls', 'created_at']
    filter_horizontal = ['select_branch', 'direction']

