import heapq


class Solution:
    # def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    #     h1, h2 = [], []
    #     for i in sorted(slots1):
    #         if not h1 or h1[0]

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1))
        slots2 = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots2))

        slot1 = sorted(slots1, key=lambda slot: slot[0])
        slot2 = sorted(slots2, key=lambda slot: slot[0])
        p1 = 0
        p2 = 0

        while p1 < len(slot1) and p2 < len(slot2):
            overlap = min(slot1[p1][1], slot2[p2][1]) - max(slot1[p1][0], slot2[p2][0])
            if overlap >= duration:
                return [max(slot1[p1][0], slot2[p2][0]), max(slot1[p1][0], slot2[p2][0]) + duration]

            if slot1[p1][0] > slot2[p2][0]:
                p2 += 1
            else:
                p1 += 1

        return []
