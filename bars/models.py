from django.db import models
from province.models import Province 
from admin_kit.models import SelectField

# Create your models here.

class Bar_Category(models.Model):
    
    bar_category_title =     models.CharField(max_length = 30, verbose_name='ジャンル')
    bar_category_eid =       models.CharField(max_length = 30, verbose_name='ジャンル (English)')
    bar_category_description = models.TextField(verbose_name='現時点で')

    def __str__(self):
        return f"{self.bar_category_title} ({self.bar_category_eid})"
    
class Bar_Facility(models.Model):
    bar_facility_title = models.CharField(max_length = 30, verbose_name='施設タイプ')
    bar_facility_eid = models.CharField(max_length = 30, verbose_name='施設タイプ (English)')
    bar_facility_description = models.TextField(verbose_name='現時点で')

    def __str__(self):
        return f"{self.bar_facility_title} ({self.bar_facility_eid})"

class Bar_Amusement(models.Model):
    bar_amusement_title = models.CharField(max_length= 50, verbose_name='アミューズメント')
    bar_amusement_eid = models.CharField(max_length= 30, verbose_name='アミューズメント (English)')
    bar_amusement_description = models.TextField(verbose_name='現時点で')
    
    def __str__(self):
        return f"{self.bar_amusement_title} ({self.bar_amusement_eid})"

class PaymentMethod(models.Model):
    paymentmethod_title = models.CharField(max_length = 50, verbose_name='支払い方法')
    paymentmethod_eid = models.CharField(max_length = 50, verbose_name='支払い方法 (English)')
    paymentmethod_description = models.TextField(verbose_name='現時点で')
    
    def __str__(self):
        return f"{self.paymentmethod_title} ({self.paymentmethod_eid})"

class Cast(models.Model):

    cast_name = models.CharField(max_length = 30, null = False, default = '', verbose_name='キャスト名')
    sex = (
        (0, '男'),
        (1, '女')
    )

    cast_sex = SelectField(choices=sex, verbose_name='性別')

    cast_birthday = models.DateField(null = True, verbose_name='誕生日')

    blood = (
        (0, 'O型'),
        (1, 'A型'),
        (2, 'B型'),
        (3, 'AB型')
    )
    cast_blood = SelectField(choices=blood, default= 0, verbose_name='血液型')
    cast_horoscope = models.CharField(max_length=20, null = True)
    # cast_photo = models.CharField(max_length= 100) => photo = [no].jpg
    cast_mobilephone = models.CharField(max_length= 30, null = True, verbose_name='携帯電話番号')
    cast_homephone = models.CharField(max_length= 30, null = True, verbose_name='家電番号')
    cast_address = models.CharField(max_length = 100, null = False, default = '', verbose_name='住所')
    cast_height = models.FloatField(null = True, verbose_name='身長')
    cast_weight = models.FloatField(null = True, verbose_name='体重')

    fk_bars =       models.ManyToManyField('Bar', through='Bar_Fk_Casts')
    
    cast_tw =        models.CharField(max_length = 30, null=True)
    cast_tiktok =    models.CharField(max_length = 30, null=True)
    cast_lin =       models.CharField(max_length = 30, null=True)
    cast_instag =    models.CharField(max_length = 30, null=True)

    cast_description = models.TextField(null = True, verbose_name='現時点で')
    
    cast_image = models.ImageField(upload_to='casts/', blank=True, null=True)

    def __str__(self):
        return f"{self.cast_name} ({self.cast_sex}, {self.cast_birthday})"




class Bar(models.Model):

    bar_title =         models.CharField(max_length = 60, verbose_name='キャスト名・店舗名', default='None')
    bar_eid =           models.CharField(max_length = 40, blank=True, null = True, verbose_name='キャスト名・店舗名 (English)')
    
    bar_main_image = models.ImageField(upload_to="bars/", blank=True, null=True)
    
    fk_province =       models.ForeignKey(Province, on_delete=models.CASCADE, null = False, verbose_name='都道府県選択')

    fk_categorys =      models.ManyToManyField('Bar_Category')
    fk_facilitys =      models.ManyToManyField('Bar_Facility')
    fk_amusements =     models.ManyToManyField('Bar_Amusement')
    fk_paymentmethods = models.ManyToManyField('PaymentMethod')

    fk_casts =          models.ManyToManyField(Cast, through='Bar_Fk_Casts')

    bar_phone=          models.CharField(max_length = 120, blank=True, null=True, verbose_name='電話')
    bar_gongij =        models.TextField(blank=True, null=True, verbose_name='お知らせ')
    bar_events =        models.TextField(blank=True, null=True, verbose_name='最新イベント')

    bar_system_worktime = models.CharField(max_length = 60, blank=True, null=True, verbose_name='システム - 営業時間')
    bar_system_rest =   models.CharField(max_length = 60, blank=True, null=True, verbose_name='システム - 定休日')
    bar_system_pay =   models.CharField(max_length = 60, blank=True, null=True, verbose_name='システム - 料金システム')
    bar_system_tax =   models.CharField(max_length = 60, blank=True, null=True, verbose_name='システム - TAX')

    bar_quiren =        models.TextField(blank=True, null=True, verbose_name='求人')
    bar_vorder =        models.IntegerField(null=True, verbose_name='現時点で', default=0)
    
    bar_map_url =       models.URLField(blank=True, verbose_name="地図情報")
    
    def __str__(self):
        return f"{self.bar_title} ( {self.id} ) [ {self.fk_province} ]"

class Bar_room(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    bar_room_label = models.CharField(max_length=10, null=True)
    bar_room_name = models.CharField(max_length=60, null=True)
    bar_room_description = models.TextField()
    
    bar_room_main_image = models.ImageField(upload_to="bars/")

    def __str__(self):
        return f"{self.bar_room_label} {self.bar_room_name}"

class Bar_Fk_Casts(models.Model):
    
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)

    bar_recorddate = models.DateField(null = True)
    bar_expiredate = models.DateField(null = True)

    def __str__(self):
        return "{}_{}".format(self.bar.__str__(), self.cast.__str__())

# in this project, not used. for future.    
class Temp_bar_cast(models.Model):
    barid = models.IntegerField(5, null = True)
    castid = models.IntegerField(5, null = True)

    def __str__(self):
        return f"{self.barid}, {self.castid}"