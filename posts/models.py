from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='image')
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
    # 작성자를 위한 코드 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 게시물에 좋아요를 누른 사람을 위한 코드
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        # related_name : 역참조를 다른 모델로 바꿔줌.
        # 만약 위에 작성자를 작성하지 않았다면, 굳이 바꾸지 않아도 됐을 것
        # 지금 user랑 like_user로 두 개가 있어서, 충돌이 일어나서 바꿔주려고 하는 것임.
        
    )

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
