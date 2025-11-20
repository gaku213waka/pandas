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

plt.rcParams['font.family'] = 'Arial Unicode MS Gothic' #windowsの方は'MS Gothic'をお試しください
plt.rcParams["figure.figsize"] = [8, 6] # 単位はインチ
plt.rcParams['font.size'] = 17
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15

＃グラフの線の指定
plt.plot(x, y, "--") #-------------になる
plt.plot(x, z, "-.") #-.-.-.-.-.-.-.になる
plt.xlim(0, 20) #ｘ軸の範囲の指定
plt.ylim(0, 22) #ｙ軸の範囲の指定

＃散布図
plt.scatter(x, y) #散布図の場合、scatterを使う
plt.scatter(x, z)
#あとは折れ線グラフと一緒





