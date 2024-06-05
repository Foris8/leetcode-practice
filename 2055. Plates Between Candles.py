from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, qs: List[List[int]]) -> List[int]:
        n = len(s)
        prefcandle = [-1] * n
        suffcandle = [float('inf')] * n
        pref = [0] * n

        # Calculate the number of plates (*) up to each position
        plates = 0
        for i in range(n):
            if s[i] == '*':
                plates += 1
            pref[i] = plates

        # Calculate the nearest left candle for each position
        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                last_candle = i
            prefcandle[i] = last_candle

        # Calculate the nearest right candle for each position
        next_candle = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                next_candle = i
            suffcandle[i] = next_candle

        # Answer each query
        result = []
        for l, r in qs:
            left_candle = suffcandle[l]
            right_candle = prefcandle[r]
            if left_candle < r and right_candle > l:
                result.append(pref[right_candle] - pref[left_candle])
            else:
                result.append(0)

        return result
