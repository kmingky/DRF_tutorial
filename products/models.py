from django.db import models

from users.models import User
from django.utils import timezone

# Create your models here.

# product 앱에서 <작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일>가 포함된 product 테이블을 생성해주세요
class ProductCategory(models.Model):
    name = models.CharField("상품카테고리", max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField("제목", max_length=50)
    thumbnail = models.FileField("썸네일", upload_to='uploads/thumbnail/%Y/%m/%d/')
    detail_image = models.FileField("상세이미지", upload_to='uploads/detail/%Y/%m/%d/')
    product_categoy = models.ForeignKey(ProductCategory, verbose_name="상품카테고리", on_delete=models.SET_NULL, null=True)
    description = models.TextField("설명")
    register_date = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_start_date = models.DateTimeField("노출시작일", default=timezone.now)
    exposure_end_date = models.DateTimeField("노출종료일", default=timezone.now)

    def __str__(self):
        return f"{self.user.username}의 {self.title}"


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="상품")
    name = models.CharField("상품옵션명", max_length=20)
    price = models.IntegerField("상품가격")