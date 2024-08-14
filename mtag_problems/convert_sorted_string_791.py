class Solution:
    """
    2 way
    1st - create an empty result.Add everything from S in result. Use comparator on order and based on position,
        sort using comparator the result and then return .
    2nd way: OPTIMAL
        create a hashmap, add all the content from S in hashmap and also the count of each character in S as values.
        Then iterate through order to get order and for each character in order, goto hashmap and
        append each charater to result as per their count.
        then whatever is remaining in map, attach them as well in result and return it.
    """
    def customSortString(self, order: str, s: str) -> str:
        frequexy_map = {}
        for i in range(len(s)):
            frequexy_map[s[i]] = 1 + frequexy_map.get(s[i], 0)
        result = ""
        for ord in order:
            if ord in frequexy_map:
                for u in range(frequexy_map[ord]):
                    result = result + ord
                del frequexy_map[ord]

        for key in frequexy_map.keys():
            for u in range(frequexy_map[key]):
                result = result + key
        return result


    def customSortStringunpotimal(self, order: str, s: str) -> str:
        # Convert the string s into a list of characters
        result = list(s)

        # Define the custom comparator using the sorted function
        result.sort(key=lambda c: order.index(c) if c in order else len(order))

        # Return the result as a string
        return ''.join(result)
