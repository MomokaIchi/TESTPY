import requests

API_KEY = "7a637fc5eb0d4707a35076cfd7107eb9"
url = "https://api.odpt.org/api/v4/odpt:TrainInformation"

params = {
    "acl:consumerKey": API_KEY,
    "odpt:operator": "odpt.Operator.Toei"
}

res = requests.get(url, params=params)

print("ステータスコード:", res.status_code)
print("レスポンス本文:", res.text)  # ←ここで中身を見てみる

if res.status_code == 200:
    try:
        data = res.json()
        print("取得件数:", len(data))
    except Exception as e:
        print("JSONとして読み込めません:", e)
else:
    print("エラーが発生しました。")
