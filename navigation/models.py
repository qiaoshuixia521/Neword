from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField('名字',max_length=20)
    image = models.ImageField('封面图',upload_to='assets/%Y/%m')
    describe = models.TextField()

    def __str__(self):
        return self.name

    class Meta:     #mtea 类用于附加描述模型的元数据
        ordering = ["name"]     #指定模型默认的排序方式
        verbose_name = "最佳人物排行榜"
        verbose_name_plural = "最佳排行榜"
