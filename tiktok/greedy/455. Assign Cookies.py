class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        g_point = 0
        s_point = 0

        count = 0

        while g_point < len(g) and s_point < len(s):
            if s[s_point] >= g[g_point]:
                count += 1
                s_point += 1
                g_point += 1
            else:
                g_point += 1

        return count
