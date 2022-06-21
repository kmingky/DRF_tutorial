from django.db import models

from users.models import User
from django.utils import timezone

# Create your models here.

# product 앱에서 <작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일>가 포함된 product 테이블을 생성해주세요
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to='uploads/%Y/%m/%d/')
    description = models.TextField("설명")
    register_date = models.DateTimeField("등록일자", default=timezone.now)
    exposure_start_date = models.DateTimeField("노출시작일", default=timezone.now)
    exposure_end_date = models.DateTimeField("노출종료일", default=timezone.now)

    def __str__(self):
        return f"{self.user.username}의 {self.title}"
