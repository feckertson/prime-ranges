'''
findMaximalRun(2)
{'length': 1, 2: 0}

findMaximalRun(3)
staringLength: 3
relevantPrimeValues: [2, 3]
Record processing time: 0.0010 seconds
{'length': 0, 'residues': [[3, 1], [5, 1]]}

findMaximalRun(5)
staringLength: 5
relevantPrimeValues: [2, 3, 5]
bestExtension
{'length': 5, 'residues': [[3, 1], [5, 1]]}
Record processing time: 0.0012 seconds
{'length': 5, 'residues': [[3, 1], [5, 1]]}

findMaximalRun(7)
staringLength: 9
relevantPrimeValues: [2, 3, 5, 7]
bestExtension
{'length': 9, 'residues': [[3, 1], [5, 1], [7, 1]]}
Record processing time: 0.0014 seconds
{'length': 9, 'residues': [[3, 1], [5, 1], [7, 1]]}

findMaximalRun(11)
staringLength: 13
relevantPrimeValues: [2, 3, 5, 7, 11]
bestExtension
{'length': 13, 'residues': [[3, 2], [5, 3], [7, 1], [11, 3]]}
Record processing time: 0.0018 seconds
{'length': 13, 'residues': [[3, 2], [5, 3], [7, 1], [11, 3]]}

findMaximalRun(13)
staringLength: 21
relevantPrimeValues: [2, 3, 5, 7, 11, 13]
bestExtension
{'length': 21, 'residues': [[3, 1], [5, 4], [7, 3], [11, 1], [13, 1]]}
Record processing time: 0.0023 seconds
{'length': 21, 'residues': [[3, 1], [5, 4], [7, 3], [11, 1], [13, 1]]}

findMaximalRun(17)
staringLength: 25
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17]
bestExtension
{'length': 25, 'residues': [[3, 2], [5, 2], [7, 1], [11, 9], [13, 1], [17, 3]]}
Record processing time: 0.0037 seconds
{'length': 25, 'residues': [[3, 2], [5, 2], [7, 1], [11, 9], [13, 1], [17, 3]]}

findMaximalRun(19)
staringLength: 33
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19]
bestExtension
{'length': 33, 'residues': [[3, 1], [5, 3], [7, 4], [11, 5], [13, 9], [17, 1], [19, 1]]}
Record processing time: 0.0072 seconds
{'length': 33, 'residues': [[3, 1], [5, 3], [7, 4], [11, 5], [13, 9], [17, 1], [19, 1]]}

findMaximalRun(23)
staringLength: 37
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23]
bestExtension
{'length': 39, 'residues': [[3, 1], [5, 1], [7, 5], [11, 5], [13, 3], [17, 5], [19, 1], [23, 1]]}
Record processing time: 0.2060 seconds
{'length': 39, 'residues': [[3, 1], [5, 1], [7, 5], [11, 5], [13, 3], [17, 5], [19, 1], [23, 1]]}

findMaximalRun(29)
staringLength: 45
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
bestExtension
{'length': 45, 'residues': [[3, 1], [5, 2], [7, 5], [11, 10], [13, 3], [17, 11], [19, 15], [23, 1], [29, 5]]}
Record processing time: 0.2601 seconds
{'length': 45, 'residues': [[3, 1], [5, 2], [7, 5], [11, 10], [13, 3], [17, 11], [19, 15], [23, 1], [29, 5]]}

findMaximalRun(31)
staringLength: 57
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
bestExtension
{'length': 57, 'residues': [[3, 1], [5, 1], [7, 6], [11, 4], [13, 10], [17, 5], [19, 9], [23, 17], [29, 1], [31, 1]]}
Record processing time: 0.6426 seconds
{'length': 57, 'residues': [[3, 1], [5, 1], [7, 6], [11, 4], [13, 10], [17, 5], [19, 9], [23, 17], [29, 1], [31, 1]]}

findMaximalRun(37)
staringLength: 61
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
bestExtension
{'length': 65, 'residues': [[3, 1], [5, 1], [7, 3], [11, 3], [13, 10], [17, 11], [19, 9], [23, 11], [29, 1], [31, 9], [37, 1]]}
Record processing time: 46.3779 seconds
{'length': 65, 'residues': [[3, 1], [5, 1], [7, 3], [11, 3], [13, 10], [17, 11], [19, 9], [23, 11], [29, 1], [31, 9], [37, 1]]}

findMaximalRun(41)
staringLength: 73
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
bestExtension
{'length': 73, 'residues': [[3, 2], [5, 3], [7, 5], [11, 7], [13, 2], [17, 14], [19, 1], [23, 9], [29, 21], [31, 25], [37, 1], [41, 3]]}
Record processing time: 22.1742 seconds
{'length': 73, 'residues': [[3, 2], [5, 3], [7, 5], [11, 7], [13, 2], [17, 14], [19, 1], [23, 9], [29, 21], [31, 25], [37, 1], [41, 3]]}

>>> findMaximalRun(43)
staringLength: 81
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
bestExtension
{'length': 89, 'residues': [[3, 1], [5, 3], [7, 3], [11, 1], [13, 7], [17, 4], [19, 10], [23, 22], [29, 10], [31, 15], [37, 1], [41, 1], [43, 9]]}
maxCoverageSkipCount: 388579986
noHitsSkipCount: 2412550214
Record processing time: 2251.9696 seconds
{'length': 89, 'residues': [[3, 1], [5, 3], [7, 3], [11, 1], [13, 7], [17, 4], [19, 10], [23, 22], [29, 10], [31, 15], [37, 1], [41, 1], [43, 9]]}

>>> findMaximalRun(47)
staringLength: 85
relevantPrimeValues: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
bestExtension
{'length': 89, 'residues': [[3, 1], [5, 1], [7, 3], [11, 5], [13, 12], [17, 9], [19, 9], [23, 10], [29, 17], [31, 15], [37, 7], [41, 19], [43, 28], [47, 42]]}
bestExtension
{'length': 99, 'residues': [[3, 1], [5, 2], [7, 2], [11, 9], [13, 10], [17, 15], [19, 4], [23, 16], [29, 23], [31, 27], [37, 27], [41, 19], [43, 26], [47, 42]]}
maxCoverageSkipCount: 5541674619
noHitsSkipCount: 35057815100
Record processing time: 66431.3234 seconds
{'length': 99, 'residues': [[3, 1], [5, 2], [7, 2], [11, 9], [13, 10], [17, 15], [19, 4], [23, 16], [29, 23], [31, 27], [37, 27], [41, 19], [43, 26], [47, 42]]}  

'''

#there is probably opportunity to improve the maximumEssentialCoverage calculation.

import itertools
import time

class ResidueOption:
  def __init__(self, prime, value, extensionLength):
    self.prime = prime
    self.value = value
    self.extensionLength = extensionLength
    self.coveredPositions = set()
    position = prime-value-1
    while position < extensionLength:
      self.coveredPositions.add(position)
      position += prime
    self.lengthEndCovered = {extensionLength: self.extensionLength - self.prime in self.coveredPositions}
      
      
  def extend(self, length):
    if length > self.extensionLength:
      self.extensionLength = length
      position = max(self.coveredPositions) + self.prime
      while position <= self.extensionLength:
        self.coveredPositions.add(position)
        position += self.prime
      self.lengthEndCovered[length] = self.extensionLength - self.prime in self.coveredPositions


class RelevantPrime:
  def __init__(self, value, length):
    self.value = value
    self.length = length
    #maximumEssentialCoverage is incorrect for 2, but that hardly matters.
#    self.maximumEssentialCoverage = (((length-1)//value)//2) + 1
    self.maximumEssentialCoverage = (((length-2)//value)//2) + 1
    self.residueOptions = []
    for residue in range(1, value):
      self.residueOptions.append(ResidueOption(value, residue, length))
  
  def extend(self, length):
    self.length = length
#    self.maximumEssentialCoverage = (((length-1)//self.value)//2) + 1
    self.maximumEssentialCoverage = (((length-2)//self.value)//2) + 1
    for residueOption in self.residueOptions:
      residueOption.extend(length)


class Approximation:
  bestLength = 0
  bestResidues = []
#  maxCoverageSkipCount = 0
#  noHitsSkipCount = 0
  
  def __init__(self, approximation, residueOption):
    if approximation == None:
      self.length = residueOption.extensionLength
      self.residueOptions = [residueOption]
      self.uncoveredPositions = [n for n in range(self.length) if n%2 == 1 and n not in residueOption.coveredPositions]
    else:
      self.length = approximation.length
      self.residueOptions = approximation.residueOptions.copy()
      self.residueOptions.append(residueOption)
      self.uncoveredPositions = [n for n in approximation.uncoveredPositions if n not in residueOption.coveredPositions ]
      
  def print(self):
    print({'length': self.length, 'residues': [[ro.prime, ro.value] for ro in self.residueOptions]})


def extendApproximation(approximation, remainingPrimes):
  global maximumEssentialCoverages
  #approximation.print()
  #print(f'remainingPrimes: {[rp.value for rp in remainingPrimes]}')
  #print(f'uncoveredPositions: {approximation.uncoveredPositions}')
  remainingPrimesLength = len(remainingPrimes)
  if remainingPrimesLength == 0:
    if len(approximation.uncoveredPositions) == 0:
      grow(approximation)
      return approximation
    else:
      return None
  if len(approximation.uncoveredPositions) > maximumEssentialCoverages[remainingPrimesLength]:
    #print("exiting recursion for lack of space")
    #Approximation.maxCoverageSkipCount += 1
    return None
  bestExtension = None
  tailPrimes = remainingPrimes[1:]
  for residueOption in remainingPrimes[0].residueOptions:
    if any(position in residueOption.coveredPositions for position in approximation.uncoveredPositions):
      extension = extendApproximation(Approximation(approximation, residueOption), tailPrimes)
      if extension != None:
        if Approximation.bestLength < extension.length:
#          print(f"Previous Approximation.bestLength: {Approximation.bestLength}")
          Approximation.bestLength = extension.length
          Approximation.bestResidueOptions = extension.residueOptions
          bestExtension = extension
#          print(f"Approximation.bestLength: {Approximation.bestLength}")
          print("bestExtension")
          extension.print()
#    else:
#      Approximation.noHitsSkipCount += 1
        
  return bestExtension


def grow(approximation):
  global relevantPrimes
  global maximumEssentialCoverages
  
  needToGrow = False
  for residueOption in approximation.residueOptions:
    if residueOption.lengthEndCovered[approximation.length]:
      needToGrow = True
      break
  
  if needToGrow:
#    print("need to grow")
#    approximation.print()
    newLength = approximation.length
    done = False
    while not done:
      done = True
      for residueOption in approximation.residueOptions:
        if (newLength + residueOption.value + 1) % residueOption.prime == 0:
#          print(f'newLength: {newLength}')
#          print(f'residueOption.prime: {residueOption.prime}')
#          print(f'residueOption.value: {residueOption.value}')
          done = False
          break
      newLength = newLength + 2
    newLength -= 2
    approximation.length = newLength
    if newLength > Approximation.bestLength:
      for relevantPrime in relevantPrimes:
        relevantPrime.extend(newLength)
      maximumEssentialCoverages = list(itertools.accumulate([relevantPrime.maximumEssentialCoverage for relevantPrime in reversed(relevantPrimes)]))
#      print(f'newLength: {newLength}')
#      print(f'maximumEssentialCoverages: {maximumEssentialCoverages}')


def primesUpTo(n):
    isPrime = [True] * (n+1)
    isPrime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    return [i for i, v in enumerate(isPrime) if v]


def findMaximalRunL(N, L):
  global relevantPrimes
  global maximumEssentialCoverages
  
  if N < 2:
    return {'length': 0}
  if N < 3:
    return {'length': 1, 2: 0}
      
  start_time = time.perf_counter()
  
  relevantPrimeValues = primesUpTo(N)
  ceilingPrime = relevantPrimeValues[-2]
  if L == 0:
    L = 2*ceilingPrime-1
    
#  Approximation.length = L
  Approximation.bestLength = 0
  Approximation.bestResidues = []
#  Approximation.maxCoverageSkipCount = 0
#  Approximation.noHitsSkipCount = 0
  
  relevantPrimes = [RelevantPrime(p, L) for p in relevantPrimeValues]
  maximumEssentialCoverages = list(itertools.accumulate([relevantPrime.maximumEssentialCoverage for relevantPrime in reversed(relevantPrimes)]))
  print(f'staringLength: {L}')
  print(f'relevantPrimeValues: {relevantPrimeValues}')
#  print(f'maximumEssentialCoverages: {maximumEssentialCoverages}')
#  print(f'2-residueOptions count: {len(relevantPrimes[0].residueOptions)}')
#  print(f'2-residueOptions[0].value: {relevantPrimes[0].residueOptions[0].value}')
#  print(f'lengthEndCovered: {[[ro.prime, ro.value] for rp in relevantPrimes for ro in rp.residueOptions if ro.lengthEndCovered[L]]}')
  
  maximalRun1 = extendApproximation(Approximation(None, ResidueOption(3, 1, L)), relevantPrimes[2:])
  maximalRun2 = extendApproximation(Approximation(None, ResidueOption(3, 2, L)), relevantPrimes[2:])
  
  #print(f'maxCoverageSkipCount: {Approximation.maxCoverageSkipCount}')
  #print(f'noHitsSkipCount: {Approximation.noHitsSkipCount}')
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Record processing time: {elapsed_time:.4f} seconds")  
    
  return {'length': Approximation.bestLength, 'residues': [[ro.prime, ro.value] for ro in Approximation.bestResidueOptions]}    


def findMaximalRun(N):
  return findMaximalRunL(N, 0)


# provide the list of odd resdiues for a starting point and a target length
# outputs the starting point and the next length/2 odd values.
def printRun(start, length):
  start = [1] + start
  for i in range(0, length+1, 2):
    if i%2 == 0:
      print([(start[j]+i)%primes[j] for j in range(1, len(start))])

# provide the list of odd resdiues for a starting point
# outputs the starting point and all subsequent odd values until the next RP value.
def printMaximalRun(start):
  start = [1] + start
  print([start[j] % primes[j] for j in range(1, len(start))])
  nextOdd = [(start[j] + 2)%primes[j] for j in range(len(start))]
  while 0 in nextOdd:
    print([nextOdd[j] % primes[j] for j in range(1, len(start))])
    nextOdd = [(nextOdd[j] + 2)%primes[j] for j in range(len(start))]
  print([nextOdd[j] % primes[j] for j in range(1, len(start))])
