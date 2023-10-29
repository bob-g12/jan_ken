from django.contrib import admin

# 同じディレクトリにあるmodels.pyからクラスのAccountをインポート
from .models import Account

# 管理ページに登録
admin.site.register(Account)