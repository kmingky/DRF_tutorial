from django.db import models
from users.models import User

# Create your models here.
# <카테고리 이름, 설명>
class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name

# <글 작성자, 글 제목, 카테고리, 글 내용>
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("내용")

    def __str__(self):
        return f"{self.user.username}의 게시물"

# blog 앱에 <게시글, 사용자, 내용>이 포함된 comment 테이블을 작성해주세요
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="게시글")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    contents = models.TextField("내용")