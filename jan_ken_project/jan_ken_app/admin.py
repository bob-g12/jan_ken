from django.contrib import admin

# モデルをインポート
from .models import Account

# 管理ツールに登録
admin.site.register(Account)