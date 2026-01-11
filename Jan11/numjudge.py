text = input("何か入力してください: ")

# 1. 10進数（半角・全角）のみか？
if text.isdecimal():
    print("10進数のみです。")
elif text.isdigit(): # 10進数以外（例:  superscript 1）も判定したい場合
    print("数字（10進数以外も含む）です。")
elif text.isnumeric(): # 漢数字なども判定したい場合
    print("数として扱える文字です（漢数字など）。")
else:
    print("数字ではありません。")
