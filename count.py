def main():
    import random
    loop = 10
    limit = 100
    count = 0
    even = 0
    odd = 0
    totalEven = 0
    totalOdd = 0
    while (count < loop):
        num = 0
        while (num < limit):
            ran_num = random.randint(1, 1000)
            num += 1
            if (ran_num % 2 == 0):
                even += 1
            elif (ran_num % 2 != 0):
                odd += 1

            totalEven = even
            totalOdd = odd
                
        print("Even:", totalEven, "Odd:", totalOdd)
        even -= even
        odd -= odd
        count += 1
        print(count)
    print("End")     
main()