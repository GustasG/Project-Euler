summation :: Integer -> Integer -> Integer
summation k n =
    k * p * (p + 1) `div` 2 where
        p = (n - 1) `div` k


multiples :: Integer -> Integer
multiples number =
    summation 3 number +
    summation 5 number -
    summation 15 number


main = do
    print(multiples limit)
    where
        limit = 1000