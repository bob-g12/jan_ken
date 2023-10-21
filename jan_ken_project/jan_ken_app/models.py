# モデル読込
from django.db import models

# モデルクラスを作成
class People(models.Model):
	# 項目定義
    Name     = models.CharField(max_length=100)           # 文字列 最大文字数100
    Tell     = models.IntegerField(blank=True, null=True) # 整数
    Mail     = models.EmailField(max_length=100)          # Email
    Birthday = models.DateField()                         # 日付
    Website  = models.URLField()                          # URL
    FreeText = models.TextField()                         # フリーテキスト

    # テキスト表示
    def __str__(self):
    	return self.Name