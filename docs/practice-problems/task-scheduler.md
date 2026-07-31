---
title: Leetcode 621 - Task Scheduler
tags:
  - leetcode
  - neetcode-150-list
  - python
  - heap
  - queue
  - greedy
updated_date: 2026-07-30
url: https://leetcode.com/problems/task-scheduler/
---

# Leetcode 621 - Task Scheduler

## Understanding the Problem

We are given a list of tasks represented by capital letters. Each task takes exactly **1 unit of time** to execute, and the same task must have a cooldown period of `n` time units before it can be executed again.

The objective is to determine the **minimum total time** required to complete all tasks, where idle intervals are allowed whenever no task is available.

A greedy strategy works well here by always executing the task with the **highest remaining frequency** whenever possible.

### Why execute the most frequent task first?

The tasks with the highest frequencies are the hardest to schedule because they require the most cooldown gaps between consecutive executions. If we postpone these tasks, we may eventually run out of other tasks to fill those cooldown periods, forcing unnecessary idle intervals.

By scheduling the most frequent task as early as possible:

- We start its cooldown immediately, allowing other tasks to naturally fill the waiting period.
- We reduce the risk of having several copies of the same task left near the end, where there may not be enough distinct tasks to separate them.
- Less frequent tasks are easier to fit into the schedule since they have fewer remaining occurrences.

For example, suppose:

```text
tasks = [A, A, A, B, C], n = 2
```

If we delay `A` and execute `B` and `C` first:

```text
B C A idle idle A idle idle A
```

we introduce many unnecessary idle intervals because only `A` remains.

Instead, executing the most frequent task first gives:

```text
A B C A idle A
```

where the cooldowns are naturally filled by the other available tasks, producing a shorter schedule.

This is why we always choose the task with the largest remaining frequency.

---

To efficiently manage task execution, we use two data structures:

- **Max Heap:** Stores the remaining frequencies of all tasks. The task with the highest remaining count is always selected first.
- **Queue:** Stores tasks currently in their cooldown period as `(remaining_count, available_time)`.

At every unit of time:

1. Increment the current time.
2. If the heap is not empty, execute the most frequent available task.
3. Decrease its remaining frequency.
4. If it still has remaining occurrences, place it into the cooldown queue with the earliest time it can be executed again (`current_time + n`).
5. Before moving to the next iteration, check whether the task at the front of the queue has completed its cooldown. If so, move it back into the heap.

Since tasks are inserted into the queue in chronological order, the task at the front is always the next one whose cooldown expires.

> 💡 **Why do we use `time + n` instead of `time + n + 1`?**
>
> The task is executed during the current time unit. By the time we reach the cooldown check at the end of the loop, one unit of time has already elapsed. Therefore, storing `available_time = time + n` ensures the task becomes available exactly after `n` cooldown intervals.

---

## Solution Implementation

### Code

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict = Counter(tasks)
        max_heap = [-v for v in count_dict.values()]
        heapq.heapify(max_heap)

        queue = deque()  # (remaining_count, available_time)

        time = 0

        while max_heap or queue:
            time += 1

            # Execute the most frequent available task
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1

                # If the task still has occurrences remaining,
                # place it into cooldown.
                if cnt:
                    queue.append((cnt, time + n))

            # Reinsert tasks whose cooldown has finished
            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(max_heap, task)

        return time
```

### Time Complexity

Let:

- $T$ = total number of tasks
- $K$ = number of distinct task types

Each task is:

- Removed from the heap once for every execution.
- Inserted back into the heap after each cooldown (except its final execution).
- Added to and removed from the cooldown queue once per cooldown.

Each heap operation costs $O(\log K)$.

Therefore:

**Overall time complexity — $O(T \log K)$**

### Space Complexity

The algorithm stores:

- A frequency map with at most $K$ entries.
- A max heap containing at most $K$ task frequencies.
- A cooldown queue containing at most $K$ waiting tasks.

Therefore:

**Overall space complexity — $O(K)$**

---

## Additional Resources

- https://neetcode.io/problems/task-scheduling
- https://leetcode.com/problems/task-scheduler/