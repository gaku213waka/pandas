import pandas as pd
import matplotlib.pyplot as plt #matplotlibはグラフを作成するために必要なライブラリ
df = pd.read_csv("data/test_data4.csv")#csvファイルの読み込み

x = df.x
y = df.y
z = df.z #それぞれの列の要素を変数に代入

＃折れ線グラフ

plt.plot(x, y)　#対応する関係を打ち込む
plt.plot(x, z)
plt.title("折れ線グラフ")　#タイトルの名前を設定
plt.xlabel("x")　#横軸の名前の設定
plt.ylabel("y"or"z")　#縦軸の名前の設定
plt.legend(["y", "z"])　#グラフの名前を表示
plt.show()　#命令

＃フォントとグラフのサイズ
plt.reParams["font.family"] = "Arial Unicode MS"　#フォントの指定
#Windowsの場合：Arial Unicode MS　→　MS Gothicに直す
plt.reParams["figure.figsize"] = [8, 6] #グラフのサイズを指定（単位はインチ）１インチ＝2.54cm
plt.reParams["font.size"] = 17 #文字のサイズ
plt.reParams["xtick.labelsize"] = 15 #x軸のメモリのサイズの指定
plt.reParams["ytick.labelsize"] = 15 #y軸のメモリのサイズの指定

＃グラフの線の指定
plt.plot(x, y, "--") #-------------になる
plt.plot(x, z, "-.") #-.-.-.-.-.-.-.になる
plt.xlim(0, 20) #ｘ軸の範囲の指定
plt.ylim(0, 22) #ｙ軸の範囲の指定

＃散布図
plt.scatter(x, y) #散布図の場合、scatterを使う
plt.scatter(x, z)
#あとは折れ線グラフと一緒

＃円グラフ
x_labels = ["A", "B", "C"]　#ラベルをリストで生成
plt.pie(x, labels=x_labels)　#円グラフを描くための関数
plt.pie(x, labels=x_labels, startangle=90, concerclock=False)
#startangleはどこから始めるか、concerclockは回転方向：Trueなら反時計、Falseなら時計周り
plt.pie(x, label = x_label, startangle=90, concerclock=False, autopct=lambda f:"{:.1f}".format(f) if f > 5 else "")
#fが5より大きかったら少数1桁の％表示する。fが5以下なら""を返す。
plt.title("円グラフ")
plt.show()





