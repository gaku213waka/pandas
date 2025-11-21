import pandas as pd
df ＝ pd.read＿csv（”data/test＿data2.csv”, skiprows＝[981, 982] #skiprowで指定した行を飛ばす。
df["都道府県名"] == "岩手県" #都道府県名という列に岩手県が存在するか確かめる。
(df["都道府県名"] == "岩手県" | df["都道府県名"] == "宮城県") #条件

flit = (df["都道府県名"] == "岩手県")
df[flit].head(10) #条件に当てはまる情報のみを取得

df.loc[flit, ["都道府県名", "総人口"]].head(10) #条件の中から措定した列の情報を取得
df.loc[~flit, ["都道府県名", "総人口"]].head(10) #条件に当てはまらない指定された列の取得

prefecture_list = ["山梨県", "奈良県", "長野県"]
filt = df["都道府県名"].isin(prefecture_list) #データフレームの中に、prefecture_listの要素が入っているかを確認
extracted_df = df[flit] #新しいデータフレームの作成

filt = extracted_df["都道府県名"].isin(["奈良県"]) #都道府県名に奈良県が含まれているか確認
extracted_df.drop(index = extracted_df[flit].index) #条件のインデックスだけ出力、drop関数でインデックスの当てはまる列を削除

