from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    # 제목
    title = models.CharField(max_length=200)

    # 내용
    content = models.TextField()

    # 작성자 (User와 N:1 관계)
    # settings.AUTH_USER_MODEL -> 커스텀 User 까지 대응
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    # 작성일 (생성 시 자동 기록)
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정일 (수정 시 자동 갱신)
    updated_at = models.DateTimeField(auto_now=True)
