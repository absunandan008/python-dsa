class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or portion == "":
                continue
            else:
                stack.append(portion)
        final_str = "/" + "/".join(stack)
        '''
        simplified_path = '/'
        for i, dir in enumerate(stack):
            simplified_path += dir
            if i < len(stack) - 1:
                simplified_path += '/'
        return simplified_path
        '''

        return final_str

# Test cases
test_cases = [
    "/home/",
    "/home//foo/",
    "/home/user/Documents/../Pictures",
    "/../",
    "/.../a/../b/c/../d/./"
]

solution = Solution()
for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {solution.simplifyPath(case)}")
    print()