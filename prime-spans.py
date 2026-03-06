# Approximation objects are the residue values for the initial primes up to some maximum prime p
# along with a predicated length and the number of items in the target lenth not killed by the gven starting value. 
# Every prime must be essential for some value in a maximal run. Otherwise it could be repurposed to kill the final value ending the run.


import time
import copy

def findMaximalRun(p, n):
  return findMaximalRunM(p, n, 0)


# finds the length and a starting point for a maximal run of consecutive integers of which at most m are relatively prime to every prime upt to p.
# n is a "suggestion" for a minimum result 
def findMaximalRunM(p, n, m):
  global g_maxRunStart
  global g_maxRunLength
  global g_maxP
  start_time = time.time()
  m = 2*(m//2)
  initialize(p, n, m)  
  for i in [1, 2]:
    approximation = createInitialApproximation(i, m)
    extendIt(approximation)
  end_time = time.time()
  print("time: {0}".format(end_time - start_time))
  if (g_maxRunStart[g_maxP] > 0):
    return {'runLength': g_maxRunLength, 'start': g_maxRunStart}
  return "No such run is possible"

#DOES THIS WORK ???
#It only asks if the trailing primes can kill all but the target number of relatively prime values in the current maxrange from the current start


def extendIt(approximation):
  global g_options
  global g_maxRunLength
  global g_maxRunStart
  global g_maxP
  global g_rpCap
  global g_minKill
#  print("extendIt: ", approximation)
  if len(approximation['rpIndexes']) < g_rpCap + g_minKill[approximation['nextPrime']]:
#    print('lengthen rpIndexes too small')
    lengthen(approximation)
  if approximation['maxValuedP'] < g_maxP:
    if not extendible(approximation):
      return
    nextPrime = approximation['nextPrime']
    nextNextPrime = primes[1 + prime_idx[nextPrime]]
    extension = copy.deepcopy(approximation)
    extension['nextPrime'] = nextNextPrime
    extension['maxValuedP'] = nextPrime
    for i in g_options[nextPrime]:
#    for i in [j for j in g_options[nextPrime] if (-j)%nextPrime in approximation['rpIndexes']]:
      extension['values'][nextPrime] = i
      extension['rpIndexes'] = copy.deepcopy(approximation['rpIndexes'])
      for idx in extension['rpIndexes']:
        if (i + idx) % nextPrime == 0:
          extension['rpIndexes'].remove(idx)
#      print("extendIt.setRunLength", extension['runLength'], extension)
      setRunLength(extension, extension['runLength'])
      extendIt(extension)
  else:
#    print('terminal approximation:', approximation)
# THIS WAS ALREADY DONE AT THE VERY BEGINNING - g_minKill[g_maxP^] = 0
    if len(approximation['rpIndexes']) < g_rpCap:
#      print('lengthen terminal rpIndexes too small')
      lengthen(approximation)
    if len(approximation['rpIndexes']) == g_rpCap:
#      print('terminal approximation:', approximation)
#      print('g_maxRunLength:', g_maxRunLength, 'g_maxP:', g_maxP, 'g_maxRunStart:', g_maxRunStart)
#      if (approximation['runLength'] > g_maxRunLength or (g_maxRunStart[g_maxP] == -1 and approximation['runLength'] == g_maxRunLength)) and isValidFinalApproximation(approximation):
      if (approximation['runLength'] > g_maxRunLength or (g_maxRunStart[g_maxP] == -1 and approximation['runLength'] == g_maxRunLength)):
        print('terminal approximation setMaxRunLength:', approximation['runLength'], approximation)
        setMaxRunLength(approximation['runLength'])
        g_maxRunStart = copy.deepcopy(approximation['values'])
#        print('g_maxRunStart:', g_maxRunStart)


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
#    print("lengthen.setRunLength", runLength, approximation)
    setRunLength(approximation, runLength)
#    if approximation['runLength'] > g_maxRunLength:
#      g_maxRunStart = copy.deepcopy(approximation['values'])
#      print("set lengthen g_maxRunStart: ", approximation)
#     setMaxRunLength(approximation['runLength'])
#  print("leaving lengthen: ", approximation)


def setRunLength(approximation, runLength):
  approximation['runLength'] = runLength
#  global g_options
#  print('setRunLength', runLength, approximation)
#  for p in approximation['values']:
#    approximation['endValues'][p] = (approximation['values'][p] + runLength)%p 
#  endValues = [(approximation['values'][p] + runLength)%p for p in g_options if p <= approximation['maxValuedP']]
#  while 0 in endValues:
#    runLength = runLength + 2
#    endValues = [(approximation['values'][p] + runLength)%p for p in g_options if p <= approximation['maxValuedP']]
#  approximation['runLength'] = runLength
#  for i in range(len(endValues)):
#    approximation['endValues'][primes[1+1]] = endValues[i]
#  print('runLength', runLength)
#  return runLength


def extendible(approximation):
  global g_rpCap
  global g_maxKill
  global g_maxRunLength
  global g_options
#  if approximation['runLength'] < g_maxRunLength:
#    approximation['rpIndexes'].extend(
#      [i for i in range(approximation['runLength'], g_maxRunLength, 2) if not 0 in [(i + approximation['values'][p])%p for p in g_options if p <= approximation['maxValuedP']]]
#    )
#    print('extendible.setRunLength', g_maxRunLength, approximation)
#    setRunLength(approximation, g_maxRunLength)
#  print('extendible')
#  print(approximation)
# print("g_maxKill: ", g_maxKill)
  if len(approximation['rpIndexes']) - g_maxKill[approximation['nextPrime']] > g_rpCap:
#    print("False")
    return False
#  print("True")
  return True


def isValidFinalApproximation(approximation):
#  print('isValidFinalApproximation - ', approximation)
  global g_options
  if next((i for i in approximation['rpIndexes'] if next((p for p in g_options if (i + approximation['values'][p])%p != p-1), -1) == -1), -1) != -1:
#    print('False')
    return False
#  print('True')
  return True;


def setMaxRunLength(M):
  global g_maxRunLength
  global g_maxKill
  global g_options
  if M > g_maxRunLength:
    g_maxRunLength = M
    mm1 = M - 1
    killMax = 0
    for p in reversed(g_options):
      killMax = killMax + 1 + mm1//p
      g_maxKill[p] = killMax


def initialize(p, n, m):
  global g_maxP
  global g_rpCap
  global g_options
  global g_maxRunStart
  global g_maxRunLength
  global g_minKill
  global g_maxKill
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


# creates an empty approimation to the prime residues for the starting value of a run and then adds i = 1,2 as the residue for 3
def createInitialApproximation(i, M):
  global g_maxRunStart
  global g_minKill
  global g_options
  global g_rpCap
  approximation = dict()
  approximation['values'] = dict()
#  approximation['endValues'] = dict()
  approximation['maxValuedP'] = 3
  approximation['rpIndexes'] = []
  for q in g_options:
    approximation['values'][q] = -1
#    approximation['endValues'][q] = -1
    if (i == 1):
      g_maxRunStart[q] = -1
  runLength = 2
  rpCount = 0
  while rpCount < g_rpCap + g_minKill[5]:
    if (i + runLength)%3 != 0:
      rpCount = rpCount + 1
      approximation['rpIndexes'].append(runLength)
    runLength = runLength + 2
  if (i + runLength)%3 == 0:
    runLength = runLength + 2
  approximation['runLength'] = runLength
  approximation['values'][3] = i
#  approximation['endValues'][3] = (runLength + i)%3
  approximation['nextPrime'] = 5
  if (i == 1):
    if M == 0:
      setMaxRunLength(runLength)
    else:
      setMaxRunLength(M)
    g_maxRunStart = copy.deepcopy(approximation['values'])
#  print("initialApproximation: ", approximation)
  return approximation


def printRun(start, length):
  start = [1] + start
  for i in range(length+1):
    print([(start[j]+i)%primes[j] for j in range(len(start))])

def printRun(start, length):
  start = [1] + start
  for i in range(0, length+1, 2):
    if i%2 == 0:
      print([(start[j]+i)%primes[j] for j in range(1, len(start))])


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

