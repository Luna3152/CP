# 問題URL

https://leetcode.com/problems/two-sum/description/

# 学んだこと

## Two Sum問題の解法

- すぐに思いつくのは全探索。[3,4,2]の場合、最初に3を取って残りの4,2と足してtargetの数になるものがあるか探索。
  - これだと2重のforループを使う必要があるため、 $O(n^2)$.
- 本質的な考え方は、 辞書を一つ準備して与えられたリスト内のvalueとインデックスを格納していく。target - iがこの辞書の中にあるかをみていって、あった時点でreturnを実行して出力。
- 本質的には以下の部分
```
            if complement_target in seen:
                return [seen[complement_target], i]
            seen[num] = i
```
