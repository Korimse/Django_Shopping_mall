from django.db import models


class Djuser(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=32, verbose_name="비밀번호")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "djuser"
        verbose_name = "고객"
        verbose_name_plural = "고객"
