def findMaximalRun(p, n):
  global maxP
  global rpCap
  global options
  global bestChoice 
  global maxRunStart
  global maxRunLength
  bestChoice = dict()
  approximation = initialize(p, n)
  extendIt(approximation)
  #print ("bestChoice: {0}".format(bestChoice))
  return {'runLength': maxRunLength, 'start': maxRunStart}


def extendIt(approximation):
  global bestChoice
  global options
  global maxRunLength
  global maxRunStart
#  print("approximation:\n{0}".format(approximation))
  if approximation['maxValuedP'] < maxP:
    extension = approximation.copy()
#    bestExtension = approximation.copy()
    nextPrime = primes[1 + prime_idx[extension['maxValuedP']]]
    extension['maxValuedP'] = nextPrime
    for i in options[nextPrime]:
      extension['values'][nextPrime] = i
      extendIt(extension)
  else:
    runLength = getRunLength(approximation)
    if runLength > maxRunLength:
      maxRunLength = runLength
      for p in options:
        maxRunStart[p] = approximation['values'][p]
      bestChoice = approximation.copy()


#findMaximalRun(11)


def getRunLength(approximation):
  currentValue = [approximation['values'][p] for p in options]
#  print("values: {0}".format(currentValue))
  if 0 in currentValue:
    return 0
  rpCount = 0
  runLength = -2
  while rpCount <= rpCap:
#    print("currentValue: {0}".format(currentValue))
    if not 0 in currentValue:
      rpCount = rpCount + 1
    runLength = runLength + 2
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
#  print("runLength: {0}".format(runLength))
  return runLength



def initialize(p, n):  
  global maxP
  global rpCap
  global options
  global maxRunStart
  global maxRunLength
  maxP = p
  rpCap = n + 1
  maxRunLength = 0
  options = dict()
  maxRunStart = dict()
  approximation = dict()
  approximation['values'] = dict()
  approximation['maxValuedP'] = 2
  for q in [q for q in primes if q > 2 and q <= p]:
    options[q] = list(reversed(range(1, q)))
    approximation['values'][q] = -1
    maxRunStart[q] = -1
  return approximation


findMaximalRun(5, 1)

