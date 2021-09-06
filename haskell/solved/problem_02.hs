fib n =
  table !! n where
    table = 1 : 1 : zipWith (+) table (tail table)


evenFibSum limit =
  sum(filter even fibValues) where
    fibValues = takeWhile (<limit) (map fib [1..])


main = do
  print (evenFibSum limit)
  where
  limit = 4000000