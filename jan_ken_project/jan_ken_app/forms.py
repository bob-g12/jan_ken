from django import forms
#モデルクラスを呼出
from .models import People

#フォームクラス作成
class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = People

        #②表示するモデルクラスのフィールドを定義
        fields = ('Name','Tell','Mail','Birthday','Website','FreeText')

        #③表示ラベルを定義
        labels = {'Name':"名前",
                  'Tell':"電話番号",
                  'Mail':"メール",
                  'Birthday':"生年月日",
                  'Website':"Webサイト",
                  'FreeText':"備考",
        }