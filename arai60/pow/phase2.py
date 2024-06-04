"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/45/files
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/41/files
x^nをx^n/2 * x^n/2と見るか, x^2 * n/2と見るかで書き方がことなるのがみれた。前者は僕のphase1, 後者は上の2人のコードに表れていた。

super_verbさん: https://discord.com/channels/1084280443945353267/1210494002277908491/1210521583605776414
phase2のコードで**演算子を使っていたが, 今回はそれの実装なのでやや微妙なのではと感じた

power内部実装, 時間がある時に読む https://qiita.com/AkariLuminous/items/ab3f382643e92122f8ef
hayashi-ayさんの実装がわかりやすそう
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int):
            if n == 0:
                return 1
            if n % 2 == 0:
                return pow(x * x, n // 2)
            else:
                return x * pow(x * x, (n - 1) // 2)
        if n < 0:
            return 1 / pow(x, -n)
        return pow(x, n)