#!/usr/bin/python3

def main():
    numerator_multip = 1
    denominator_multip = 1

    for numerator in range(10, 100):
        for denominator in range(11, 100):
            if numerator >= denominator or (numerator % 10 == 0 and denominator % 10 == 0):
                continue

            numerator_str = str(numerator)
            denominator_str = str(denominator)

            for char in numerator_str:
                if char in denominator_str:
                    numerator_str = numerator_str.replace(char, '')
                    denominator_str = denominator_str.replace(char, '')

                    if len(numerator_str) == 0 or len(denominator_str) == 0:
                        continue

                    simplified_numerator = int(numerator_str)
                    simplified_denominator = int(denominator_str)

                    if simplified_numerator == 0 or simplified_denominator == 0:
                        continue

                    if simplified_numerator/simplified_denominator == numerator/denominator:
                        print('{0}/{1} == {2}/{3}'.format(simplified_numerator, simplified_denominator, numerator, denominator))
                        numerator_multip *= simplified_numerator
                        denominator_multip *= simplified_denominator


    print('Division result(not simplified): {0}/{1}'.format(numerator_multip, denominator_multip))



if __name__ == "__main__":
    main()