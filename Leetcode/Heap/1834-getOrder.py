class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)

        arr = []

        for i, (enqueue, process) in enumerate(tasks):
            arr.append((enqueue, process, i))

        arr.sort()

        pq = []

        ans = []

        time = 0
        i = 0

        while i < n or pq:

            if not pq and time < arr[i][0]:
                time = arr[i][0]

            while i < n and arr[i][0] <= time:
                enqueue, process, idx = arr[i]

                heappush(pq, (process, idx))
                i += 1

            process, idx = heappop(pq)

            time += process

            ans.append(idx)

        return ans
