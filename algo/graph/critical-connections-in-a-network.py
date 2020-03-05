class Solution:
    def criticalConnections(n, connections):
        """
        :param connections: List[List[int]]
        :return: List[List[int]]
        """
        graph = [[] for i in range(n)]
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        lows = [n]*n
        critical = []

        def dfs(node, discovery_time, parent):
            if lows[node] == n:
                lows[node] = discovery_time
                for neighbor in graph[node]:
                    if neighbor != parent:
                        expected_discovery_time_of_child = discovery_time + 1
                        actual_discovery_time_of_child = dfs(neighbor, expected_discovery_time_of_child, node)
                        if actual_discovery_time_of_child >= expected_discovery_time_of_child:
                            critical.append((node, neighbor))

                        # low will be equal to discovery time of this node or discovery time of child
                        # whichever one is minm
                        # if its discovery time of child - then there is a backpath
                        lows[node] = min(lows[node], actual_discovery_time_of_child)

            # return low of this node discovered previously or during this call
            return lows[node]

        dfs(n - 1, 0, -1)

