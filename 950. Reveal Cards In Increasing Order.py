class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # [2,3,5,7,8,11,13,17]
        # 2, 8, 3, 11, 5, 13, 7, 17

        N = len(deck)
        queue = deque()

        for i in range(N):
            queue.append(i)

        deck.sort()

        res = [0] * N

        for card in deck:
            res[queue.popleft()] = card

            if queue:
                queue.append(queue.popleft())

        return res
