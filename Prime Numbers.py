def primes_method2(n):
    out = list()
    for num in range(1, n + 1):
        print(list(num % i != 0 for i in range(2, num)), num)
        if all(num % i != 0 for i in range(2, num)):
            out.append(num)
    return out


"""So it places a list of [1,2,3,4,...n+1] so that the last number is included.
        Then is takes the first iteration which is 1 and places it into the range(2,num).
                which is range(2,1) which is blank until we reach iteration 3.
                    The first two are 1 % NONE and 2 % NONE which give NONE

                Now we're onto 3, range(2,3) gives [2]
                    Is 3 % 2 != 0 ? you get 1.5 which doesn't equal 3.
                        So we place 3 into the out.append(num)

                Now we're on 4, range(2,4) gives [2,3]
                    Is 4 % 2 != 0, well is does 0 != 0 is False, so because we have all()
                    this number would get get added into out.append(num)

                    let's finsh the list..

                    Is 4 % 3 != 0, you get 1.3333.. and so True, but again because of the above
                    we would not add in the number 4 as a prime number

                Now we're on 5, range(2,5) gives [2,3,4]
                    .....


"""

print(primes_method2(10))

""""
[]
1
[]
2
[True]
3
[False, True]
4
[True, True, True]
5
[False, False, True, True]
6
[True, True, True, True, True]
7
[False, True, False, True, True, True]
8
[True, False, True, True, True, True, True]
9
[False, True, True, False, True, True, True, True]
10
[1, 2, 3, 5, 7]

"""