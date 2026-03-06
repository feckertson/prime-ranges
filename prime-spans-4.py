import time
import copy

def findMaximalRun(p, n):
  return findMaximalRunM(p, n, p*(n+1))


def findMaximalRunM(p, n, m):
  global g_maxRunStart
  global g_maxRunLength
  global g_approximationChain
  start_time = time.time()
  m = 2*(m//2)
  initialize(p, n, m)  
  for i in [1, 2]:
    approximation = createInitialApproximation(i)
    g_approximationChain = [approximation]
    extendIt(approximation)
  end_time = time.time()
  print("time: {0}".format(end_time - start_time))
  return {'runLength': g_maxRunLength, 'start': g_maxRunStart}


#DOES THIS WORK ???
#It only asks if the trailing primes can kill all but the target number of relatively prime values in the current maxrange from the current start


def extendIt(approximation):
  global g_options
  global g_maxRunLength
  global g_maxRunStart
  global g_maxP
  global g_rpCap
  global g_minKill
  global g_approximationChain
#  print("extendIt: ", approximation)
  if len(approximation['rpIndexes']) < g_rpCap + g_minKill[approximation['nextPrime']]:
#    print('lengthen rpIndexes too small')
    lengthen(approximation)
  if approximation['maxValuedP'] < g_maxP:
    if not extendible(approximation):
      g_approximationChain.remove(approximation)
      return
    nextPrime = approximation['nextPrime']
    nextNextPrime = primes[1 + prime_idx[nextPrime]]
    extension = copy.deepcopy(approximation)
    extension['nextPrime'] = nextNextPrime
    extension['maxValuedP'] = nextPrime
    for i in g_options[nextPrime]:
      extension['values'][nextPrime] = i
      extension['rpIndexes'] = copy.deepcopy(approximation['rpIndexes'])
      for idx in extension['rpIndexes']:
        if (i + idx) % nextPrime == 0:
          extension['rpIndexes'].remove(idx)
      g_approximationChain.append(extension)
      extendIt(extension)
  else:
#    print('terminal approximation:', approximation)
    if len(approximation['rpIndexes']) < g_rpCap:
#      print('lengthen terminal rpIndexes too small')
      lengthen(approximation)
#    print('terminal approximation:', approximation)
#    print('g_maxRunLength:', g_maxRunLength)
#    print('g_maxRunStart:', g_maxRunStart)
    if approximation['runLength'] > g_maxRunLength:
#      print('terminal approximation setMaxRunLength:', approximation['runLength'])
      setMaxRunLength(approximation['runLength'])
      g_maxRunStart = copy.deepcopy(approximation['values'])
    if approximation['runLength'] == g_maxRunLength and len(approximation['rpIndexes']) == g_rpCap:
      g_maxRunStart = copy.deepcopy(approximation['values'])
#      print("set terminal g_maxRunStart: ", g_maxRunStart)
  g_approximationChain.remove(approximation)


def lengthen(approximation):
  global g_rpCap
  global g_minKill
  global g_options
  global g_maxRunLength
  global g_maxRunStart
#  print("lengthen: ", approximation)
  runLength = approximation['runLength']
  rpCount = len(approximation['rpIndexes'])
  rpLimit = g_rpCap + g_minKill[approximation['nextPrime']]
  if rpCount < rpLimit:
    while rpCount < rpLimit:
      if 0 not in [(runLength + approximation['values'][p])%p for p in g_options if p <= approximation['maxValuedP']]:
        approximation['rpIndexes'].append(runLength)
        rpCount = rpCount + 1
      runLength = runLength + 2
#      print(approximation)
  while 0 in [(runLength + approximation['values'][p])%p for p in g_options if p <= approximation['maxValuedP']]:
    runLength = runLength + 2
  approximation['runLength'] = runLength
  if runLength > g_maxRunLength:
    g_maxRunStart = copy.deepcopy(approximation['values'])
#    print("set lengthen g_maxRunStart: ", g_maxRunStart)
    setMaxRunLength(runLength)
#  print("leaving lengthen: ", approximation)


def extendible(approximation):
  global g_rpCap
  global g_maxKill
  global g_maxRunLength
  global g_options
  if approximation['runLength'] < g_maxRunLength:
    approximation['rpIndexes'].extend(
      [i for i in range(approximation['runLength'], g_maxRunLength, 2) if not 0 in [(i + approximation['values'][p])%p for p in g_options if p <= approximation['maxValuedP']]]
    )
    approximation['runLength'] = g_maxRunLength
#  print('extendible')
#  print(approximation)
# print("g_maxKill: ", g_maxKill)
  if len(approximation['rpIndexes']) - g_maxKill[approximation['nextPrime']] > g_rpCap:
#    print("False")
    return False
#  print("True")
  return True


def isBetterRunLength(approximation, M):
  global g_options
  global g_rpCap
  print("isBetterRunLength - ", M, approximation)
  currentValue = [approximation['values'][p] for p in g_options]
  if 0 in currentValue:
    return 0
  rpCount = 0
  for i in range(M//2 - 1):
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
    if not 0 in currentValue:
       rpCount = rpCount + 1
    if rpCount == g_rpCap + 1:
      return False
  return True


def getRunLength(approximation):
  global g_options
  global g_rpCap
  currentValue = [approximation['values'][p] for p in g_options]
#  print("values: {0}".format(currentValue))
  if 0 in currentValue:
    return 0
  rpCount = 0
  runLength = 0
  while rpCount < 1+g_rpCap:
#    print("currentValue: {0}".format(currentValue))
    currentValue = [(2 + currentValue[prime_idx[p]-1]) % p for p in approximation['values']]
    runLength = runLength + 2
    if not 0 in currentValue:
      rpCount = rpCount + 1
#  print("runLength: {0}".format(runLength))
  return runLength


def setMaxRunLength(M):
  global g_maxRunLength
  global g_maxKill
  global g_approximationChain
  global g_options
  if M > g_maxRunLength:
    g_maxRunLength = M
    mm1 = M - 1
    killMax = 0
    for p in reversed(g_options):
      killMax = killMax + 1 + mm1//p
      g_maxKill[p] = killMax
#    print('g_approximationChain: ', g_approximationChain)
    for approximation in g_approximationChain:
      if approximation['runLength'] < M:
        widenApproximation(approximation, M)
#    print('g_approximationChain: ', g_approximationChain)


def widenApproximation(approximation, M):
  approximation['rpIndexes'].extend([i for i in range(approximation['runLength'], M) if 0 not in [(i + approximation['values'][p])%p for p in g_options if p <= approximation['maxValuedP']]])
  approximation['runLength'] = M


def initialize(p, n, m):
  global g_maxP
  global g_rpCap
  global g_options
  global g_maxRunStart
  global g_maxRunLength
  global g_minKill
  global g_maxKill
  global g_approximationChain
  g_maxP = p
  g_rpCap = n
  g_options = dict()
  g_maxRunStart = dict()
  for q in [q for q in primes if q > 2 and q <= p]:
    g_options[q] = list(range(1, q))
    g_maxRunStart[q] = -1
  g_minKill = dict()
  g_maxKill = dict()
  killMin = 0
  for p in reversed(g_options):
    killMin = killMin + 1
    g_minKill[p] = killMin
  g_minKill[primes[1+prime_idx[g_maxP]]] = 0
  g_maxRunLength = 0
  g_approximationChain = []


def createInitialApproximation(i):
  global g_maxRunStart
  global g_minKill
  global g_options
  global g_rpCap
  approximation = dict()
  approximation['values'] = dict()
  approximation['maxValuedP'] = 3
  approximation['rpIndexes'] = []
  for q in g_options:
    approximation['values'][q] = -1
    g_maxRunStart[q] = -1
  approximation['values'][3] = i
  runLength = 2
  rpCount = 0
  while rpCount < g_rpCap + g_minKill[5]:
    if (i + runLength)%3 != 0:
      rpCount = rpCount + 1
      approximation['rpIndexes'].append(runLength)
    runLength = runLength + 2
  approximation['runLength'] = runLength
  approximation['nextPrime'] = 5
  if (i == 1):
    setMaxRunLength(runLength)
    g_maxRunStart = copy.deepcopy(approximation['values'])
#  print("initialApproximation: ", approximation)
  return approximation


def printRun(start, length):
  start = [1] + start
  for i in range(length+1):
    print([(start[j]+i)%primes[j] for j in range(len(start))])


def printRunS(start, length):
  printRun([start[i] for i in start], length)


def printRunCC(start, cap):
  startval = [1] + start
  rpCount = 0
  runLength = 0
  while rpCount < cap+2:
    currentValue = [(startval[i] + runLength) % primes[i] for i in range(len(startval))]
    if 0 not in currentValue:
      rpCount = rpCount+1
      print(currentValue, "*")
    else:
      print(currentValue)
    runLength = runLength + 1
  print("runLength: ", runLength-1)
  


def printRunC(start, cap):
  rpCount = 0
  runLength = 0
  while rpCount < cap+2:
    currentValue = [(1+runLength)%2] + [(start[p] + runLength)%p for p in start]
    if 0 not in currentValue:
      rpCount = rpCount+1
      print(currentValue, "*")
    else:
      print(currentValue)
    runLength = runLength + 1
  print("runLength: ", runLength-1)
  

findMaximalRun(5, 1)

