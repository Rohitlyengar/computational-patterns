class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]

        stack = []

        for pos, speed in sorted(pair):
            time = (target - pos) / speed

            if stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
