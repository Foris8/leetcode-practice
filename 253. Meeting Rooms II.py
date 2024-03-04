class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        free_room = []

        heapq.heappush(free_room, intervals[0][1])

        for i in intervals[1:]:
            # 30 <- incoming 10
            if free_room[0] <= i[0]:
                heapq.heappop(free_room)

            # add it into the heap q

            heapq.heappush(free_room, i[1])

        return len(free_room)
