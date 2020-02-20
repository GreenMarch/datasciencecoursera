# This approach mimics the method of meeting room 2.
# Idea is to first sort the trips in the order of the start times.
# 1. Push the following details of first trip into the priority queue [end_time, capacity]. Also decrement this capacity from the total capacity.
# 2. select trips and check if the end_time of the trip in priority_queue is less than/equal the start time of the current trip. If its true then remove it from the pqueue while increasing the capacity.
# If the end time is greater than start_time of the current trip then check if the additional capacity from the current trip be accomodated. If yes, then update capacity and push this trip into priority queue, else return False.
import heapq
class Solution:
    def carPooling(self, trips, capacity):
        trips = sorted(trips, key=lambda x: x[1])
        # print(trips)
        heap = []
        # heapq.heappush(heap, [trips[0][2], trips[0][0]])

        for i in range(0, len(trips)):
            c2, s2, e2 = trips[i]
            # print(heap)
            if not heap:
                if capacity < c2:
                    return False
                capacity -= c2
                heapq.heappush(heap, [e2, c2])
                # print("trip: {}, capacity: {}".format(i, capacity))
            else:
                e1, c1 = heapq.heappop(heap)
                capacity += c1
                while heap and s2 >= e1:
                    e1, c1 = heapq.heappop(heap)
                    capacity += c1

                if not heap and s2 >= e1:
                    if capacity < c2:
                        return False
                    capacity -= c2
                    heapq.heappush(heap, [e2, c2])
                else:

                    if capacity >= c1 + c2:
                        capacity -= (c1 + c2)
                        heapq.heappush(heap, [e1, c1])
                        heapq.heappush(heap, [e2, c2])
                        # print("trip: {} capacity: {}".format(i, capacity))
                    else:
                        return False

        return True

data = [[2,1,5],[3,3,7]]
print(Solution().carPooling(data))