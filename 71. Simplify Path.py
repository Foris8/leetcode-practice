class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        res = ""
        stack = []

        for ele in path:
            if stack and ele == "..":
                stack.pop()

            elif ele != "" and ele != ".." and ele != ".":
                stack.append(ele)
        return "/" + "/".join(stack)
