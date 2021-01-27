Binary Search
- Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. I the value of the search key is less than
in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value if found or the interval is
empty.

- Run Time = O(log N)
