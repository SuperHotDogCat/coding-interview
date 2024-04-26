"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/43/files
bisectの引数で探索範囲を絞れることを知る。ただ, この場合rightの調整にphase1で作ったものよりも一工夫必要で, numsのとりうるindexより+1しないとダメだった
ちょっと調べてみたところhttps://docs.python.org/ja/3.6/library/bisect.html
このようにbisectの引数が[lo:hi]となるスライスの中を探しているからだった。

hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/49/files
考察の
nums[i]とnums[-1]を比較してnums[i]の方が大きい場合は左側は昇順に並んでいる。それ以外の場合は右側が昇順に並んでいる。
targetが昇順に並んでいる側の範囲にあればそちらを見に行く。そうでなければ反対側を見に行く。
を利用して, 1回のbinary searchでindexを見つけることができていた。認知負荷的には重い気がしたけど, 効率を求めると良い場合があるのかもしれない。
leetcode上での計測結果は誤差の範囲だった。

"""
import bisect

# 最小値のindexを見つけてそこで左右に分割して考えると分割したところは増加列になっていることを利用する
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _find_minimum_index():
            # 最小値の数がどこにあるかをO(logN)で見つける
            left = 0
            right = len(nums) - 1
            while left != right:
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return right
        
        min_index = _find_minimum_index()
        if nums[min_index] <= target <= nums[-1]:
            left = min_index
            right = len(nums)
        else:
            left = 0
            right = min_index
        
        # targetを探す
        target_index = bisect.bisect_left(nums, target, left, right)
        
        if nums[target_index] == target:
            return target_index
        return -1