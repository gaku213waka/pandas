import pandas as pd #pandasのimport

import pandas as pd
s = pd.Series([10, 20, 30], name="score")　#1列のデータの入力
print(s)

df = pd.DataFrame({
    "name": ["Tanaka", "Sato", "Suzuki"], #DataFrame化
    "score": [80, 90, 70]
})
print(df)

#データの読み込み
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df = pd.read_json("data.json")

#データの確認
df.head()        # 先頭5行
df.tail()        # 最後の5行
df.info()        # 型・欠損など
df.describe()    # 統計情報
df.columns       # 列名一覧
df.shape         # 行数・列数

#列の抽出
df[["name", "score"]]
#行の抽出（条件）
df[df["score"] >= 80]
#行番号で抽出
df.iloc[0]          # 1行目
df.iloc[0:3]        # 1〜3行
#行名（index）での抽出
df.loc[0]
df.loc[0:2]

#新しい列の追加
df["pass"] = df["score"] >= 60
df["score2"] = df["score"] * 1.1
df["full_name"] = df["name"] + "_san"

#欠損地の処理
df.dropna()          # NaN を含む行を削除
df.fillna(0)         # NaN を 0 で埋める
df["score"] = df["score"].fillna(df["score"].mean())  # 列ごとに埋める

#並び替え
df.sort_values("score")                 # 昇順
df.sort_values("score", ascending=False)  # 降順










