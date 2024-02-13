class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, state, time = log.split(":")
            fn, time = int(fn), int(time)

            if state == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time

                stack.append(fn)
                prev_time = time
            else:
                finish_fn = stack.pop()
                ans[finish_fn] += time - prev_time + 1
                prev_time = time + 1

        return ans
