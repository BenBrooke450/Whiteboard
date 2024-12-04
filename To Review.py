







def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        list2 = []
        number = [[str(x) for x in str(numbers)] for numbers in range(left, right+1) if numbers % 10 != 0 and "0" not in str(numbers)]

        a = list(filter(lambda nums: all(map(lambda y : int("".join(nums)) % int(y) == 0 ,(y for y in nums))) ,(nums for nums in number)))

        b = list(map(lambda x: int("".join(x)),a))

        return b