## Arrays & Hashing

**Trigger:** "have I seen this before?" / "how many of X" -> use a set or hashmap

- **Contains Duplicate:** track seen values in a set; if it's already there, duplicate.  Set lookup is O(1) -> one pass O(n) instead of nested lopps O(n^2).
- **Valid Anagram:** count characters. Two strings are anagrams if their character counts match. Use a hashmap (or Counter) for each, then compare.
  Trigger: "same characters, different order?" -> count and compare.
- **Two Sum:** use a hash map to store numbers you've seen so far and their indices.