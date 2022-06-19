from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # createsuperuser 시 해당 내용만 받음
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=200)
    email = models.EmailField("이메일 주소", max_length=100)
    fullname = models.CharField("이름", max_length=50)
    address = models.CharField("주소", max_length=256, null=False)

    join_date = models.DateTimeField("가입일", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} / {self.fullname}"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


# 유저에 맞는 프로필 생성
class UserProfile(models.Model):

    GENDER_CHOICE = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )

    user = models.OneToOneField(User, verbose_name="유저", on_delete=models.CASCADE)
    gender = models.CharField("성별", max_length=10, choices=GENDER_CHOICE)
    introduction = models.TextField("자기소개", null=True, blank=True)
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")
    hobby = models.ManyToManyField('Hobby', verbose_name="취미")

    def __str__(self):
        return f"{self.user.username}의 프로필"

# 취미 카테고리
class Hobby(models.Model):
    name = models.CharField("취미", max_length=20)
    def __str__(self):
        return self.name