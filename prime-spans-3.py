import time

def findMaximalRun(p, n):
  global maxP
  global rpCap
  global options
  global maxRunStart
  global maxRunLength
  start_time = time.time()
  approximation = initialize(p, n)
  extendIt(approximation)
  end_time = time.time()
  print("time: {0}".format(end_time - start_time))
  return {'runLength': maxRunLength, 'start': maxRunStart}


#DOES THIS WORK ???
#It only asks if the trailing primes can kill all but the target number of relatively prime values in the current maxrange from the current start


def extendIt(approximation):
  global options
  global maxRunLength
  global maxRunStart
  if approximation['maxValuedP'] < maxP:
    if not extendible(approximation, maxRunLength):
      return
    extension = approximation.copy()
    nextPrime = primes[1 + prime_idx[extension['maxValuedP']]]
    extension['maxValuedP'] = nextPrime
    for i in options[nextPrime]:
      extension['values'][nextPrime] = i
#      print("extendIt - {0}, {1}".format(extension, maxRunLength))
      extendIt(extension)
  else:
    if isBetterRunLength(approximation, maxRunLength):
      maxRunLength = getRunLength(approximation)
      for p in options:
        maxRunStart = approximation['values'].copy()



#Can this be improved by trackikng the relatively prime locations and associated run lengths inside of the approximations?
#Rather than visiting every value in the range across all primes each time, just count the set of them.
#extensions will reduce the (small) set which will be extended if the current max run length beats the assocated run length.
#

def extendible(approximation, runLength):
#  print("extendible - {0}, {1}".format(runLength, approximation))
  if runLength == 0:
    return True
  rpCount = 0
  currentValue = [approximation['values'][p] for p in options if p <= approximation['maxValuedP']]
  for pos in range(runLength//2 - 1):
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in options if p <= approximation['maxValuedP']]
    if not 0 in currentValue:
       rpCount = rpCount + 1
  killMax = sum([(runLength-1)//p + (approximation['values'][p] + (runLength-1)%p)//p for p in options if p > approximation['maxValuedP']])
  if killMax + rpCap < rpCount:
#     print("Not Extensible - {0}, {1}".format(runLength, approximation))
    return False
  return True





def isBetterRunLength(approximation, M):
  currentValue = [approximation['values'][p] for p in options]
  if 0 in currentValue:
    return 0
  rpCount = 0
  for i in range(M//2 - 1):
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
    if not 0 in currentValue:
       rpCount = rpCount + 1
    if rpCount == rpCap + 1:
      return False
  return True
  

def getRunLength(approximation):
  currentValue = [approximation['values'][p] for p in options]
#  print("values: {0}".format(currentValue))
  if 0 in currentValue:
    return 0
  rpCount = 0
  runLength = 0
  while rpCount < 1+rpCap:
#    print("currentValue: {0}".format(currentValue))
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
    runLength = runLength + 2
    if not 0 in currentValue:
      rpCount = rpCount + 1
#  print("runLength: {0}".format(runLength))
  return runLength



def initialize(p, n):  
  global maxP
  global rpCap
  global options
  global maxRunStart
  global maxRunLength
  maxP = p
  rpCap = n
  maxRunLength = 0
  options = dict()
  maxRunStart = dict()
  approximation = dict()
  approximation['values'] = dict()
  approximation['maxValuedP'] = 2
  for q in [q for q in primes if q > 2 and q <= p]:
    options[q] = list(range(1, q))
    approximation['values'][q] = -1
    maxRunStart[q] = -1
  return approximation


findMaximalRun(5, 1)

