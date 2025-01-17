# 概要
愚直な方法では正解できません．  
求めるべきことを明らかにして考えてみましょう．

問題原案：kusirakusira

# 解説
操作後の $A$ の要素は非常に大きくなりうるため，実際に操作を再現して答えを求めることは難しいです．  
別なアプローチを考えてみましょう．  

$P_i$ を $i$ 番目に小さい素数とします．

整数 $X = P_1^{k_1} \cdot P_2^{k_2} \cdot P_3^{k_3} \cdots$ の約数の個数は $(k_1 + 1) (k_2 + 1) (k_3 + 1) \cdots$ と表されます．  
$X$ のもつ $i$ 番目の素因数を $0$ 個以上 $k_i$ 個以下選ぶ組み合わせの総数です．

$A_i = P_1^{k_1} \cdot P_2^{k_2} \cdot P_3^{k_3} \cdots$ の値を，ベクトル $K_i = (k_1, k_2, k_3, \ldots)$ として持つことを考えます．  

すると，$Q$ 回の操作は各々次のように言い換えることができます：
- $x \eqqcolon P_1^{c_1} \cdot P_2^{c_2} \cdot P_3^{c_3} \cdots$ とする．
- $l \leq i \leq r$ を満たす任意の整数 $i$ について：
    - $K_i$ を $K_i + (c_1, c_2, c_3, \ldots)$ で置換する．

以上の操作はimos法を用いるなどして簡単に実装できます．  

求めるべきは，$E = (1, 1, 1, \ldots)$ として，$D_i = E \cdot (K_i + E))$ です．

なお実際には $A_i, x \leq 100$ より各ベクトルの要素数は高々 $25$ で十分と分かります．これは $100$ 以下の素数の個数です．  

解説：uni_kakurenbo

# 実装例
```cpp:C++
#include <cstdint>
#include <ios>
#include <iostream>
#include <valarray>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>

#include <atcoder/modint>

using i32 = std::int32_t;
using i64 = std::int64_t;
using mint = atcoder::modint998244353;

#define REP(i,n) for(i32 i=0, i##_length=i32(n); i<i##_length; ++i)

__attribute__((constructor)) inline void fast_io() { std::ios::sync_with_stdio(false), std::cin.tie(nullptr); }


constexpr i32 PRIMES[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 };

// 素因数分解
std::valarray<i32> factorize(i32 x) {
    std::valarray<i32> res(std::size(PRIMES));
    REP(i, res.size()) {
        const i32 p = PRIMES[i];
        while(x%p == 0) ++res[i], x /= p;
    }
    return res;
}

void solve() {
    i32 n; std::cin >> n;
    std::vector powers(n+1, std::valarray<i32>(std::size(PRIMES)));

    std::vector<i32> a(n, 1);

    i32 q; std::cin >> q;
    REP(_, q) {
        i32 l, r, x; std::cin >> l >> r >> x; --l;
        const auto factors = factorize(x);
        powers[l] += factors, powers[r] -= factors;  // imos法 (差分加算)
    }

    REP(i, n) powers[i+1] += powers[i];  // imos法 (累積)

    std::transform(
        powers.begin(), std::prev(powers.end()),
        std::ostream_iterator<i64>(std::cout, " "),
        [](const auto& k) -> i32 {
            return (
                std::transform_reduce(
                    std::begin(k), std::end(k),
                    mint{1}, std::multiplies<mint>{}, [](const i32 e) -> mint { return e + 1; }
                ).val()
            );
        }
    );
    std::cout << "\n";
}

signed main() {
    i32 $; std::cin >> $;
    while($--) solve();
    return 0;
}

```
