---
title: Leetcode 271 - Encode and Decode Strings
tags:
  - leetcode
  - neetcode-150-list
  - python
  - string
updated_date: 2026-07-29
url: https://leetcode.com/problems/encode-and-decode-strings/
---

# Leetcode 271 - Encode and Decode Strings

## Understanding the Problem

The goal is to encode a list of strings into a single string and then decode it back to the original list without ambiguity.

A simple delimiter such as `#` alone is **not sufficient**, since the strings themselves may contain the delimiter. Instead, we use **length-prefix encoding**, where every string is stored as:

```
<length>#<string>
```

For example:

```
["hello", "world", ""]
```

is encoded as:

```
5#hello5#world0#
```

During decoding:

- Read digits until reaching the delimiter `#` to determine the string length.
- Read exactly that many characters as the string.
- Advance the pointer to the beginning of the next encoded string.
- Repeat until the end of the encoded string.

The critical observation is that the decoder never searches for the next delimiter inside the string itself—it always knows exactly how many characters to consume.

---

## Solution Implementation

### Code

```python
from typing import List

class Codec:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0

        while start < len(s):
            stop = start

            while s[stop] != '#':
                stop += 1

            length = int(s[start:stop])
            word = s[stop + 1 : stop + 1 + length]
            res.append(word)

            start = stop + 1 + length

        return res
```

### Time Complexity

#### Encoding

Each character from every string is written exactly once.

For a total of `N` characters across all strings:

**Overall time complexity — $O(N)$**

#### Decoding

Each character is visited once while parsing the length fields and extracting the strings.

**Overall time complexity — $O(N)$**

---

### Space Complexity

#### Encoding

The encoded string contains every original character plus the length prefixes and delimiters.

**Overall space complexity — $O(N)$**

#### Decoding

The output list stores all decoded strings, whose total size is `N`.

**Overall auxiliary space complexity — $O(N)$**

---

## Key Takeaways

- Prefix each string with its length instead of relying on delimiters.
- Read exactly `length` characters after the delimiter during decoding.
- After decoding one string, move the pointer to:

```python
start = delimiter_index + 1 + length
```

- The pointer should always advance to the beginning of the next length field.
- Length-prefix encoding works correctly even if the strings contain `#`, digits, spaces, or any other characters.

---

## Common Pitfall

A common mistake is incorrectly updating the decoding pointer.

Incorrect:

```python
start = stop + 1
```

This moves the pointer to the beginning of the current string rather than the next encoded entry.

Correct:

```python
start = stop + 1 + length
```

This skips both the delimiter and the decoded string.

---

## Additional Resources

- https://neetcode.io/problems/string-encode-and-decode
- https://leetcode.com/problems/encode-and-decode-strings/
