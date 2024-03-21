class Solution():
    def count_unique_subsequence(self, s, start, dest, n):

        def solve_recur(s, index, curr, dest, n, path, result):
            if curr == dest:
                result.add(path)

            if index == len(s):
                return

            solve_recur(s, index + 1, curr, dest, n, path, result)
            if s[index] == 'l':
                if curr > 0:
                    solve_recur(s, index + 1, curr - 1,
                                dest, n, path + 'l', result)
            else:
                if curr + 1 < n:
                    solve_recur(s, index + 1, curr + 1,
                                dest, n, path + 'r', result)

        result = set([])
        solve_recur(s, 0, start, dest, n, '', result)
        return len(result)


s = Solution()
print(s.count_unique_subsequence('rrlrlr', 1, 2, 6))
