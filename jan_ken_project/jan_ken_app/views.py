from django.shortcuts import render
import random
from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
count = 0
counted = 0
judgment = ["jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html",
            "jan_ken/draw.html","jan_ken/win.html","jan_ken/lose.html","jan_ken/super.html"]
#ジャンケン結果をランダムにする関数
def random_def(low,high): 
    random_serect = random.randint(low,high)
    return random_serect

#ジャンケンの得点を計算する関数
def point(random_point):
    if judgment[random_point] == "jan_ken/lose.html":
        count = -1
    elif judgment[random_point] == "jan_ken/win.html":
        count = 1
    elif judgment[random_point] == "jan_ken/super.html":
        count = 5
    elif judgment[random_point] == "jan_ken/draw.html":
        count = 0
    return count

#Topページの関数
def frontpage(request):
    context = {
        "count": counted
    }
    return render(request,"jan_ken/lady.html",context)

#ランダムな結果を表示させる関数
def judgpage(request):
    global counted
    random_count = random_def(0,len(judgment)-1)
    
    counted += point(random_count)
    if counted < 10:
        not_clear = "あと"
        clear_count =str(10 - counted)
        not_point = "点"
    else:
        not_clear = ""
        clear_count = "CLEAR"
        not_point = ""
    context = {
        "count": counted,
        "score" : clear_count,
        "limit" : not_clear,
        "point" : not_point
    }
    return render(request,judgment[random_count],context)
#入力フォーム
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)