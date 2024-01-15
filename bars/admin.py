from django.contrib import admin
from .forms import BarForm, CastForm, BarRoomForm
from .models import Bar_Category, Bar_Facility, Bar_Amusement, PaymentMethod, Bar, Cast, Bar_room
from django.utils.safestring import mark_safe

# Register your models here.
class Bar_CategoryAdmin(admin.ModelAdmin):
    list_display = ('bar_category_title', 'bar_category_eid', 'bar_category_description')

class Bar_FacilityAdmin(admin.ModelAdmin):
    list_display = ('bar_facility_title', 'bar_facility_eid', 'bar_facility_description')    

class Bar_AmusementAdmin(admin.ModelAdmin):
    list_display = ('bar_amusement_title', 'bar_amusement_eid', 'bar_amusement_description')  

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('paymentmethod_title', 'paymentmethod_eid', 'paymentmethod_description')  

class BarRoomAdmin(admin.ModelAdmin):
    form = BarRoomForm
    add_form = BarRoomForm
    list_display = ('bar_room_label', 'bar_room_name', 'bar_room_description')

class BarRoomInline(admin.TabularInline):
    model = Bar_room
    extra = 1
    
class BarAdmin(admin.ModelAdmin):
    form = BarForm
    add_form = BarForm
    # inlines = [BarRoomInline]
    list_display = ('display_photo','bar_title', 'id', 'bar_eid', 'fk_province')  
    def display_photo(self, obj):
        if obj.bar_main_image:
            return mark_safe(f'<img src="{obj.bar_main_image.url}" width="100" height="100" alt="No Image"/>')
        else:
            return "No Image"
    display_photo.short_description = 'Photo'
    display_photo.allow_tags = False
    


        
class CastAdmin(admin.ModelAdmin):

    form = CastForm
    add_form = CastForm
    list_display = ('display_photo', 'cast_name', 'id', 'cast_sex', 'cast_birthday', 'cast_description', 'cast_address')

    def display_photo(self, obj):
        if obj.cast_image:
            return mark_safe(f'<img src="{obj.cast_image.url}" width="100" height="100" alt="No Image"/>')
        else:
            return "No Image"
    display_photo.short_description = 'Photo'
    display_photo.allow_tags = False

admin.site.site_header = "ぼいば 管理ページ" 
admin.site.site_title = "ぼいば 管理ページ"
admin.site.index_title = "ぼいば 管理ページ"

admin.site.register(Bar_Category,    Bar_CategoryAdmin)
admin.site.register(Bar_Facility,    Bar_FacilityAdmin)
admin.site.register(Bar_Amusement,   Bar_AmusementAdmin)
admin.site.register(PaymentMethod,  PaymentMethodAdmin)
admin.site.register(Bar, BarAdmin)
admin.site.register(Cast, CastAdmin)
# admin.site.register(Bar_room,   BarRoomAdmin)