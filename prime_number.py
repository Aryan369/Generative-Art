_minRange = int(input("Enter min range"))
_maxRange = int(input("Enter max range"))
_maxRange += 1

def primeNumber (minRange_, maxRange_) :
    _n = 0
    print("Prime numbers b/w %d and %d :" % (minRange_, maxRange_ - 1))
    for i in range(minRange_, maxRange_):  # For prime numbers from minRange_ to maxRange_
        if i > 1:
            for x in range (2, i):
                if i % x == 0:
                    break
            else:
                print(i)
                _n += 1
    print("Number of prime numbers :", _n)

primeNumber(_minRange, _maxRange)