class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # can start_i or end_i be negative> -> no
        # can start_i or end_i be pos/neg infinity (open interval) -> no
        # start_i <= end_i always? -> yes
        # interval will always be at form {start, end}? -> yes it will always be length of 2
        # are every intervals unique? -> doesn't matter
        # can we have no intervals? -> no there's at least one
        # can start and end time be non-integer (1.5 or something) -> no they're non-neg integers
        # are the intervals sorted in any way (by start time or etc) -> no
        # if one interval is [1,2] and the other is [2,3] is that overlapping -> yes. for it to not overlap it would be like [1,2], [3,4] 
       


        # intervals = [[1,2]]
        # output = [[1,2]]

        # intervals = [[2,5] [1,3]]
        # output = [[1,5]] 

        # intervals = [[4,5] [1,3]]
        # output = [[1,3], [4,5]] or  (order doesn't matter)


        # 2 intervals
        # scenario 1: they don't intersect -> choose both
        # scenario 2: 

        # [s1, e1]
        # [s2, e2]

        # submerge
        # E1 >= E2
        # Just choose the first one (longer one)

        # Nonsubmerge overlap
        # S1 <= s2 <= E1
        # E2 >= E1
        # Start is min(s1, s2) end is max(e1, e2)


        # Identical interval
        # S1 = s2
        # E1 = e2

        # TC: O(nlogn) -> sort by starting time will be nlogn, actual interval comparison would just be O(n) since we do have to look at every interval regardless if it overlaps or not

        # SC: O(n) -> if none of them overlaps then our result is just the intervals 
        # UNLESS... we just rewrite on top of given intervals (so merge intervals that overlap) then we can do this with O(1) SC 
        # nevermind, if we merge then the index offset will cause SC of O(n) per iteration 


        
        intervals.sort(key=lambda x: x[0]) # sort by first entry 

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            s1,e1 = result[-1][0], result[-1][1]  # loops back and picks end of the array
            s2,e2 = intervals[i][0], intervals[i][1]

            if s2 > e1: # no overlap
                result.append(intervals[i])
            elif e1 >= e2: # submerge
                continue
            else: # non-submerging overlap 
            #S1 <= s2 <= E1 & E2 >= E1
                result[-1][0], result[-1][1] = min(s1, s2), max(e1, e2)
            
        
        return result


    # intervals = [[1,3],[1,5],[6,7]] (sorted)

    # result = [[1,3]]

    # i = 1
    # s1, e1 = 1, 3
    # s2, e2 = 1, 5
    # result = [[min(1,1),max(3,5)]] = [[1,5]]

    # i = 2
    # s1, e1 = 1, 5
    # s2, e2 = 6, 7
    # result = [[1,5], [6, 7]]





            









