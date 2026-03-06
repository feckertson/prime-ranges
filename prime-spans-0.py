def findMaximalRun(p):
  approximation = createInitialApproximation(p)
  extension = extendIt(approximation)
  print (extension)



def extendIt(approximation): 
#  print('approximation')
#  print(approximation)
  if approximation['maxValuedP'] != approximation['maxP']:
    extension = approximation.copy()
    bestExtension = approximation.copy()
    nextPrime = primes[1 + prime_idx[extension['maxValuedP']]]
    extension['maxValuedP'] = nextPrime
    for i in reversed(range(nextPrime)):
      extension['values'][nextPrime] = i
      extendIt(extension)
      if extension['maxRunLength'] > bestExtension['maxRunLength']:
        bestExtension = extension.copy()
      print('bestExtension')
      print(bestExtension)
    return bestExtension
  else:
    runLength = getRunLength(approximation)
    if runLength > approximation['maxRunLength']:
      approximation['maxRunLength'] = runLength
      for p in approximation['values']:
        approximation['maxRunstart'][p] = approximation['values'][p]
    return approximation

findMaximalRun(5)  

def getRunLength(approximation):
  rpCount = 0
  runLength = 0
  currentValue = [approximation['values'][p] for p in approximation['values']]
  if 0 in currentValue:
    return 0
  while rpCount < 2:
    if not 0 in currentValue:
      rpCount = rpCount + 1
    runLength = runLength + 2
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
  return runLength


def createInitialApproximation(p):
  approximation = dict()
  approximation['maxP'] = p
  approximation['maxValuedP'] = 2
  approximation['options'] = dict()
  approximation['values'] = dict()
  approximation['maxRunLength'] = 0
  approximation['maxRunstart'] = dict()
  for q in [q for q in primes if q > 2 and q <= p]:
    approximation['options'][q] = list(range(q))
    approximation['values'][q] = -1
    approximation['maxRunstart'][q] = -1
  approximation['pCount'] = len(approximation['values'])
  return approximation


