import math


# From: https://en.wikipedia.org/wiki/Pentagonal_number
class Pentagonal:

    @staticmethod
    def isPentagonal(x: int) -> bool:
        if x <= 0:
            return False

        n = (math.sqrt(24*x + 1) + 1) / 6
        return n.is_integer()


    @staticmethod
    def getPantagonal(n: int) -> int:
        return (3*n*n - n) // 2


def find_pentagonal() -> int:
    pentagonals = []
    i = 0

    while True:
        i += 1
        sum = Pentagonal.getPantagonal(i)
        
        for Pj in pentagonals:
            Pk = sum - Pj
            diff = Pj - Pk

            if Pentagonal.isPentagonal(Pk) and Pentagonal.isPentagonal(diff):
                '''
                Difference between Pj and Pk is only getting bigger with larger j and k. 
                So we are looking for first appearance where Pj, Pk, sum and diff are pentagonal numbers.
                '''
                return abs(Pk - Pj)

        pentagonals.append(sum)



def main():
    print(find_pentagonal())


if __name__ == "__main__":
    main()