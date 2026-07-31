---
title: Leetcode 355 - Design Twitter
tags:
  - leetcode
  - neetcode-150-list
  - python
  - heap
  - hashmap
  - design
updated_date: 2026-07-31
url: https://leetcode.com/problems/design-twitter/
---

# Leetcode 355 - Design Twitter

## Understanding the Problem

The goal is to design a simplified version of Twitter that supports:

- Posting tweets
- Following and unfollowing users
- Retrieving the 10 most recent tweets from a user's news feed

A user's news feed should contain:

- Their own tweets
- Tweets from users they follow
- Tweets ordered from newest to oldest

The main challenge is efficiently retrieving the latest 10 tweets.

A straightforward solution would be:

1. Collect all tweets from the user and everyone they follow.
2. Sort them by timestamp.
3. Return the latest 10 tweets.

However, this approach does unnecessary work because we only need 10 tweets.

The key observation is:

> Tweets from each user are already sorted by time, so instead of looking at every tweet, we can merge multiple sorted tweet lists using a heap.

This is the same idea as **k-way merge**.

---

# Data Structure Design

## 1. Tweet Map

```python
tweet_map[userId] = [(timestamp, tweetId), ...]
```

Stores all tweets posted by each user.

Example:

```
User 1:
[
 (1, 101),
 (2, 102),
 (3, 103)
]
```

Tweets are stored in chronological order.

---

## 2. Follow Map

```python
follow_map[userId] = {followeeIds}
```

Stores the users that each user follows.

Example:

```
User 1 follows:
{2, 3, 4}
```

---

## 3. Timestamp Counter

A global counter gives every tweet a unique timestamp.

This allows tweets from different users to be compared chronologically.

---

# Optimal Approach Intuition

The key observation:

> Each user's tweets are already sorted by time.

Example:

```
User A:
A10 -> A9 -> A8 -> A7

User B:
B15 -> B14 -> B13 -> B12

User C:
C7 -> C6 -> C5 -> C4
```

The news feed is simply the merge of these sorted lists.

Instead of putting every tweet into a heap, we only maintain the newest available tweet from each user.

---

# Why Not Add All Tweets?

Suppose:

```
100 followed users
1000 tweets per user
```

A brute force approach processes:

```
100 * 1000 = 100,000 tweets
```

to return:

```
10 tweets
```

Most of the work is unnecessary.

The heap only limits the number of tweets stored, but it does not reduce the number of tweets examined.

---

# How the Optimal Approach Works

## Step 1: Add the Latest Tweet From Each User

Suppose:

```
User A:
A10, A9, A8

User B:
B15, B14, B13

User C:
C7, C6, C5
```

Instead of adding all tweets:

```
A10
A9
A8
B15
B14
B13
C7
C6
C5
```

we only add:

```
A10
B15
C7
```

The heap contains the best current candidate from each user.

---

## Step 2: Remove the Newest Tweet

The heap gives:

```
B15
```

because it is the newest tweet.

Add it to the feed:

```
Feed:
B15
```

Now we reveal the next tweet from User B:

```
B14
```

and add it to the heap.

Heap:

```
A10
B14
C7
```

---

## Step 3: Repeat Until We Have 10 Tweets

Repeat:

1. Remove the newest tweet from the heap.
2. Add it to the result.
3. Add the next older tweet from the same user.

Stop after collecting 10 tweets.

---

# Why This Works

If a user's newest tweet has not been selected, none of their older tweets can be selected.

Example:

```
User A:

A100
A99
A98
```

If `A100` is still in the heap:

- A99 cannot be newer than A100.
- A98 cannot be newer than A99.

Therefore, there is no reason to consider A99 or A98 yet.

We process tweets lazily and only reveal older tweets when needed.

---

# Solution Implementation

```python
from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        # User should see their own tweets
        self.follow_map[userId].add(userId)

        # Add newest tweet from every followee
        for user in self.follow_map[userId]:
            if self.tweet_map[user]:
                index = len(self.tweet_map[user]) - 1
                time, tweetId = self.tweet_map[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index - 1)
                )

        # Extract newest 10 tweets
        while heap and len(result) < 10:
            time, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add next older tweet from the same user
            if index >= 0:
                actual_time, next_tweet = self.tweet_map[user][index]

                heapq.heappush(
                    heap,
                    (-actual_time, next_tweet, user, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
```

---

# Complexity Analysis

Let:

- `F` = number of users followed
- `T` = total number of tweets stored

## Time Complexity

### Initial Heap Creation

We insert one tweet from each followee:

```
O(F)
```

### Retrieving 10 Tweets

Each heap operation:

```
O(log F)
```

For 10 tweets:

```
O(10 log F)
```

Overall:

```
O(F + 10 log F)
```

Since 10 is constant:

**Time Complexity: O(F log F)**

---

## Space Complexity

### Tweet Storage

Stores all tweets:

```
O(T)
```

### Follow Relationships

Stores follow connections:

```
O(F)
```

### Heap

Stores one candidate tweet per followee:

```
O(F)
```

Overall:

**Space Complexity: O(T + F)**

---

# Key Takeaways

- A heap does not automatically make a solution efficient.
- The important question is: how many elements enter the heap?
- Keeping heap size at 10 only limits memory usage.
- It does not reduce the number of tweets processed.
- When multiple sources are already sorted, think about k-way merge.
- Store only the best current candidate from each source.
- Reveal the next candidate only when needed.
- This pattern appears in:
  - Merge K Sorted Lists
  - Merge K Sorted Arrays
  - Top K problems

---

# Common Mistakes

## Mistake 1: Adding Every Tweet Into the Heap

Problem:

- Too many heap operations.
- Processes tweets that may never appear in the feed.

Fix:

- Add only the newest tweet from each user.
- Add older tweets only after selecting a newer tweet from that user.

---

## Mistake 2: Confusing Heap Size With Efficiency

Example:

```python
if len(heap) > 10:
    heapq.heappop(heap)
```

This only controls memory usage.

It does not reduce the number of tweets processed.

The important question is:

> How many tweets are inserted into the heap?

---

## Mistake 3: Timestamp and Heap Ordering Mismatch

Python provides a min heap.

If timestamps increase:

```
1, 2, 3, 4
```

the oldest tweet has priority.

To get newest tweets first, store negative timestamps:

```
-1, -2, -3, -4
```

Now the smallest value represents the newest tweet.

---

# Additional Resources

- [https://neetcode.io/problems/design-twitter](https://neetcode.io/problems/design-twitter)
- [https://leetcode.com/problems/design-twitter/](https://leetcode.com/problems/design-twitter/)
