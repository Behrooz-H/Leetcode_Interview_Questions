"""
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

#TODO Insertion Sort of any new entry and keeping the track of the mediana nd the 
class MedianFinder:
    multiset<int> data;
    multiset<int>::iterator mid;

public:
    MedianFinder()
        : mid(data.end())
    {
    }

    def addNum(int num):
        const int n = data.size();
        data.insert(num);

        if not n:                                # // first element inserte
            mid = data.begin();
        elif num < mid:                    #// median is decreased
            mid = (n & 1 ? mid : prev(mid));
        else                                    #// median is increased
            mid = (n & 1 ? next(mid) : mid);
    

    double findMedian()
    {
        const int n = data.size();
        return ((double) *mid + *next(mid, n % 2 - 1)) * 0.5;
    }
}

"""

Time complexity: O(logn)+O(1)≈O(logn).

Inserting a number takes O(logn) time for a standard multiset scheme. 4
Finding the mean takes constant O(1) time since the median elements are directly accessible from the two pointers.
Space complexity: O(n) linear space to hold input in container.

"""