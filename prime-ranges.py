import math
from itertools import combinations as comb


#identify the primes
limit_count = 1
limit_square = 4
primes = [2]
for n in range(3, 7000000):
  if n > limit_square:
    limit_square = primes[limit_count]**2
    limit_count = limit_count + 1
  if next((p for p in primes[:limit_count] if n%p == 0), 0) == 0:
    primes.append(n)  


prime_idx = dict()
for idx in range(len(primes)):
  prime_idx[primes[idx]] = idx


def primeFactors(n):
  return [p for p in primes if p in range(n+1) and n%p == 0]

def primeFactorsCapped(n, N):
  return [p for p in primes if p in range(N) and n%p == 0]

def isSquareFree(n):
  for p in primes:
    if n%(p*p) == 0:
      return False
  return True


#reutrn 1 if S is odd, -1 if S is even.
def parity(S):
  return math.ceil(2*(0.5 - len(S)%2))

def paritySum(SS):
  return sum([parity(S) for S in SS])


#subsets of S of size m
def subsetsN(S, m):
  return comb(S, m)

def subsetsNonEmpty(TT):
  ret = []  
  for n in range(1, 1+len(TT)):
    ret.extend(comb(TT, n))
  return ret

def subsetsCappedNonEmpty(TT, m):
  ret = []  
  for n in range(1, 1+m):
    ret.extend(comb(TT, n))
  return ret

def subsets(TT):
  ret = subsetsNonEmpty(TT)
  ret.extend(comb(TT, 0))
  return ret


#sets of primes below m whose product divides more values in (a, b) than expected... as in (b-a-1)%piS + a%piS >= piS)
def qualDM(a, b, m):
  ret = []
  D = b-a
  Dm1 = D-1
  P = [p for p in primes if p < m]
  Q = []
  QQ = set()
  for v in range(a+1, b):
    Q.append([p for p in P if v%p == 0])
    if Q[-1] == []:
      Q.pop();
  for S in Q:
    QQ.update(subsetsNonEmpty(S))
  for S in QQ:
    piS = math.prod(S)
    if Dm1%piS + a%piS >= piS:
      ret.append(S)
  ret.sort(key = lambda s: math.prod(s))
  ret.sort(key = lambda s: len(s))
  return ret

#sets of primes below (b-a) which have more multiples in (a, b) than expected.
def qualD(a, b):
  D = b-a
  if a < D:
    print("a cannot be less than b-a")
    return []
  if b > D*D:
    if a != D*D and a != D*D + D:
      print("b cannot be greater than b-a squared except when a is b-a squared or (b-a)(b-a+1)")
      return []
  return qualDM(a, b, D)


QUALS = dict()
for N in range(3, 501):
  QUALS[N] = sorted(qualD(N*(N-1), N*N), key=lambda S: math.prod(S))

PQUALS = dict()
for N in range(3, 1+max(QUALS)):
  PQUALS[N] = [math.prod(S) for S in QUALS[N]]

[N for N in range(3, 1+max(QUALS)) if paritySum(QUALS[N][len(QUALS[N])//2:]) < 0]
[N for N in range(3, 1+max(QUALS)) if paritySum(QUALS[N][:1+len(QUALS[N])//2]) < 0]
[paritySum(QUALS[N][len(QUALS[N])//2:]) for N in range(3, 1+max(QUALS))]  

# prime-subsets-limited - sets of primes below N whose product is below N*(N+1)
def PSL(N):
  ret = []
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  NN = N*N
  NNp1 = N*N+N
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    max_size += 1
    if max_so_far > NN:
      break
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      if piS <= NNp1:
        ret.append(S)
  return ret


[[S, [k for k in range(1, N+2) if (N-1)%math.prod(S) + (k*N)%math.prod(S) >= math.prod(S)]] for S in PSL(N)]


#the non-empty subsets S of primes at or below N for which (k*N, (k+1)*N] contains more multiples of piS than expected
#equivalently N%piS + kN%piS >= piS
#so only need to check cases where piS < (k+1)*N
def qual(N, k):
  ret = []
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  kN = k*N
  kpN = kN + N
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    max_size += 1
    if max_so_far > kN:
      break
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      if N%piS + kN%piS >= piS:
        ret.append(S)
  return ret


#non-qualifying sets (some of them)
#the non-empty subsets S of primes at or below N for which piS < n*(k+1) and (k*N, (k+1)*N] contains fewer multiples of piS than expected
#equivalently N%piS + kN%piS < piS
def nqual(N, k):
  ret = []
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  kN = k*N
  kpN = kN + N
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    if max_so_far > kN:
      break
    max_size += 1
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      if piS < kpN and N%piS + kN%piS < piS:
        ret.append(S)
  return ret



#the result of qual(N, k) in opposite order.
def qualR(N, k):
  X = qual(N, k)
  X.reverse()
  return X



#partition the qualifying sets for <N, k> by the maximum contained prime
def qualSplit(N, k):
  ret = []
  P = [p for p in prime_idx if p < N]
  P.reverse()
  Q = qual(N, k);
  for p in P:
    ret.append([S for S in Q if max(S) == p])
  return ret


#The list of <delta(SS(p)), SS(p)> over qualSplit
def qualWeight(N, k):
  ret = []
  split = qualSplit(N, k)
  for SP in split:
    ret.append([len([S for S in SP if len(S)%2 == 0])-len([S for S in SP if len(S)%2 == 1]), SP])
  return ret


#The list of <delta(SS(p)), p> over qualSplit
def qualWeightPrint(N, k):
  QW = qualWeight(N, k)
  for pair in QW:
    if len(pair[1]) > 0:
      print("{0}: {1}".format(pair[0], max(pair[1][0])))




#returns the set of pairs <v, sets whose max is v> over sets from SS and values from V
def split(SS, V):
  ret = []
  for v in V:
    SV = []
    for S in SS:
      if max(S) == v:
        SV.append(S)
    ret.append(SV)
  return ret





#faster algorithm for qual(N, K))
#the subsets S of the primes at or below N for which piS <= kN and (k*N, (k+1)*N] contains more multiples of piS than expected
def qual2(N, k):
  Q = set()
  P = [p for p in primes if p <=N]
  Nminus = N-1
  kN = k*N
  for n in range(kN+1, kN+N):
    PP = [p for p in P if n%p == 0]
    for L in range(1, 1+len(PP)):
      for S in subsetsN(PP, L):
        piS = math.prod(S)
        if N%piS + kN%piS >= piS:
          Q.add(S)
  return Q


#qualSplit but using qual2 to get the qualifying sets
#this should really be done in a reusable way.
def qual2Split(N, k):
  ret = []
  P = [p for p in prime_idx if p < N]
  P.reverse()
  Q = qual2(N, k);
  for p in P:
    ret.append([S for S in Q if max(S) == p])
  return ret



def qual2SplitMin(N, k):
  ret = []
  Q = qual2(N, k);
  for n in range(N):
    SS = [S for S in Q if min(S) == n]
    if len(SS) > 0:
      ret.append([n, SS])
  return ret

def qual2WeightMin(N, k):
  ret = []
  split = qual2SplitMin(N, k)
  for SP in split:
    ret.append([len([S for S in SP[1] if len(S)%2 == 0])-len([S for S in SP[1] if len(S)%2 == 1]), SP])
  return ret

def qual2WeightMinPrint(N, k):
  QW = qual2WeightMin(N, k)
  for pair in QW:
    print("{0}: {1}".format(pair[0], pair[1][0]))



from statistics import median

def qual2SplitMedian(N, k):
  ret = []
  Q = qual2(N, k);
  for n in range(N):
    ret.append([n, [S for S in Q if math.floor(median(S)) == n]])
  return ret


def qual2SplitMean(N, k):
  ret = []
  Q = qual2(N, k);
  for n in range(N):
    ret.append([n, [S for S in Q if sum(S)//len(S) == n]])
  return ret


#The list of <delta(SS), SS> over qual2Split
#this should really be done in a reusable way.
def qual2Weight(N, k):
  ret = []
  split = qual2Split(N, k)
  for SP in split:
    ret.append([len([S for S in SP if len(S)%2 == 0])-len([S for S in SP if len(S)%2 == 1]), SP])
  return ret

def qual2WeightPrint(N, k):
  QW = qual2Weight(N, k)
  for pair in QW:
    if len(pair[1]) > 0:
      print("{0}: {1}".format(pair[0], max(pair[1][0])))





#alternate approach for qual2Split.
def qual3Split(N, k):
  ret = []
  NN = range(k*N+N-1,k*N,-1)
  Q = qual2(N, k);
  for n in NN:
    ret.append([S for S in Q if n % math.prod(S) == 0])
    for S in ret[-1]:
      Q.remove(S)
  return ret


#qualWeight but using qual3Split
#this should really be done in a reusable way.
def qual3Weight(N, k):
  ret = []
  split = qual3Split(N, k)
  for SP in split:
    ret.append([len([S for S in SP if len(S)%2 == 0])-len([S for S in SP if len(S)%2 == 1]), SP])
  return ret

#qualWeightPrint but using qual3Weight
def qual3WeightPrint(N, k):
  QW = qual3Weight(N, k)
  for pair in QW:
    if len(pair[1]) > 0:
      print("{0}: {1}".format(pair[0], max(pair[1][0])))




#the subsets S of primes below (b-a) for which (a, b) contains more multiples of piS than expected, floor((b-a-1)/piS)
def qualI(a, b):
  ret = []
  P = [p for p in prime_idx if p < b-a]
  max_size = 0
  max_so_far = 1
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    if max_so_far > b-1:
      break
    max_size += 1
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      if (b-a-1)%piS + a%piS >= piS:
        ret.append(S)
  return ret

def qualISum(a, b):
  return 1 + paritySum(qualI(a, b))





#the subsets S of the primes at or below N for which (s, s+l] contains more multiples of piS than expected
def qualI(s, l, N):
  ret = []
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  stop = s + l
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    if max_so_far > stop:
      break
    max_size += 1
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      if l%piS + s%piS >= piS:
        ret.append(S)
  return ret


def nLeft(N, k):
  return set(qualI(k*N-1, 1, N))
  
def nRight(N, k):
  return set(qualI((k+1)*N-1, 1, N))

def nMiddle(N, k):
   return set(qualI(k*N, N-1, N))

def nWhole(N,k):
  return set(qualI(k*N-1, N+1, N))







def quals(N):
  return qual2(N, N-1)

def quals2(N):
  return qual2(N, N-1)

def quals1(N):
  return qual(N, N-1)






#calculate the sum over all sets of primes not above N the parity of S times (N-1) div S
#the result is always N-2
def subsetSum(N):
  retSum = 0
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    if max_so_far > N:
      break
    max_size += 1
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      retSum += parity(S)*((N-1)//piS)
  return retSum


#calculate the sum over all sets of primes not above N the parity of S times (N-1)*k div S
def subsetSumK(N, k):
  kN = k*N
  retSum = 0
  P = [p for p in prime_idx if p < N]
  max_size = 0
  max_so_far = 1
  for idx in range(len(P)):
    max_so_far = max_so_far*P[idx]
    if max_so_far > kN:
      break
    max_size += 1
  for ssize in range(1, max_size+1):
    for S in subsetsN(P, ssize):
      piS = math.prod(S)
      retSum += parity(S)*(((N-1)*k)//piS)
  return retSum


#calculate the sum over all sets of primes not above N (N-1) mod piS  --- the parity of S times ?
def subsetSumK2(N, k):
  return sum([(parity(S)*(N-1) % math.prod(S)) for S in subsets([p for p in prime_idx if p < N]) ])



def cnt0(N):
  return len([p for p in range(N**2-N, N**2) if p in prime_idx])

def cnt1(N):
  QQ = qual(N, N-1)
  return 1 + len([Q for Q in QQ if len(Q)%2 == 0]) - len([Q for Q in QQ if len(Q)%2 == 1])


def cnt2(N):
  ret = 0
  for S in subsets([p for p in primes if p < N]):
    if (len(S)%2 == 1):
      ret += (N-1)//math.prod(S)
    else:
      if len(S) > 0:
        ret -= (N-1)//math.prod(S)
  return ret


def cnt2_check(N):
  return N-2-cnt2(N)

def maxQualSize(N):
  ret = 1
  while math.prod(primes[:ret]) < N:
    ret += 1
  return ret-1 


def cnt3(N):
  ret = 0
  P = [p for p in prime_idx if p < N]
  for size in range(1 + maxQualSize(N)):
    for S in subsetsN(P, size):
      if (len(S)%2 == 1):
        ret += (N-1)//math.prod(S)
      else:
        ret -= (N-1)//math.prod(S)
  return 1 + ret



def SQual(N):
  ret = []
  P = [p for p in prime_idx if p < N]
  for size in range(1, 1 + maxQualSize(N)):
    for S in subsetsN(P, size):
      ret.append(S)
  return ret




def delN(N):
  ret = 0
  P = [p for p in primes if p < N]
  SS = []
  for size in range(1 + maxQualSize(N)):
    SS.extend(subsetsN(P, size))
  print(SS)
  for S in SS:
    if len(S) % 2 == 1:
      ret += (N-1)//math.prod(S)
    else:
      ret -= (N-1)//math.prod(S)
  return ret



def weight(SS):
  return (len([S for S in SS if len(S)%2 == 0]) - len([S for S in SS if len(S)%2 == 1]))

def weights(SSS):
  return [weight(SS) for SS in SSS]
  

factors = {n: [p for p in primes if p < N and n%p == 0] for n in range(N*N-N, N*N)}
  
SSP = [[S, [n for n in range(N*N-N, N*N) if n%math.prod(S) == 0]] for S in SS]

SSPU = [[p[0], sorted(p[1], key=lambda n: math.prod(factors[n]), reverse=True)[0]] for p in SSP]

SS_PT = [[n, [p[0] for p in SSPU if p[1] == n]] for n in range(N*N-N, N*N)]

SS_PT = [p for p in SS_PT if p[1] != []]


SSS = [[p, [S for S in SS if max(S) == p]] for p in primes if p < N]

SSSW = [[p[0], len([S for S in p[1] if len(S)%2 == 0]) - len([S for S in p[1] if len(S)%2 == 1])] for p in SSS]

SSE = [[(N-1)//math.prod(S), S] for S in SS]


def mu(S, N):
  piS = math.prod(S)
  II = [i for i in range(1+N*N-N, N*N) if i%piS == 0]
  return min([min(II)-N*N+N, N*N-max(II)])



SSD = [[i, [S for S in SS if mu(S, N) == i]] for i in range(1, 1 + N//2)]





#partition the maximal square-free divisors of values in (N*N-N, N*N) so that intergers within a partition are either 
#relatively prime or one divides the other.
def partition(N):
  factorizations = [[p for p in primes if p < N and n%p == 0] for n in range(1+N*N-N, N*N)]
  print( "factorizations: {0}".format(factorizations) )
  unique_factorizations = []
  [unique_factorizations.append(x) for x in factorizations if x != [] and x not in unique_factorizations]
  print( "unique_factorizations: {0}".format(unique_factorizations) )
  partition = []
  while len(unique_factorizations) > 0:
    partition_group = []
    s_group_factors = set()
    for factorization in unique_factorizations:
      s_factorization = set(factorization)
      if s_factorization.isdisjoint(s_group_factors) or s_factorization.issubset(s_group_factors) or s_factorization.issuperset(s_group_factors):
        s_group_factors |= s_factorization
        partition_group.append(factorization)
    for g in partition_group:
      unique_factorizations.remove(g)
    partition.append(partition_group)
  return partition



def qualOrg(N, k):
  SS = qual2(N, k)
  return [[p, len([S for S in SS if len(S)%2 == 0 and p in S]) - len([S for S in SS if len(S)%2 == 1 and p in S])] for p in [p for p in primes if p < N]]




def qualifyingResidues(piS):
  ret = []
  for v in range(2, piS):
    if v%piS + (v*v-v)%piS >= piS:
      ret.append(v)
  return ret


def qualCheck(N):
  QQ = quals(N)
  QQN = getQQN(N, QQ)
  QQM = [Q for Q in QQ if Q not in QQN]
  print("{0}: {1}, {2}".format(N, paritySum(QQN), paritySum(QQM)))

def check(L):
  for N in range(2, L+1):
    QQ = quals(N)
    QQN = getQQN(N, QQ)
    QQM = [Q for Q in QQ if Q not in QQN]
    if paritySum(QQN) > 0 or paritySum(QQM) > 0:
      print("{0}: {1}, {2}".format(N, paritySum(QQN), paritySum(QQM)))
    

def getQQN(N, QQ):
  return [Q for Q in QQ if max(Q) <= 2*N//3]




for n in range(5, 100):
  if isSquareFree(n):
    print("{0}: {1}".format(n, qualifyingResidues(n)))




SSP = [[]]
for p in primes[0:5]:
  SSP1 = []
  for S in SSP:
    T = S.copy()
    T.append(p)
    SSP1.append(T)
  SSP.extend(SSP1)


for S in SSP:
  QS = []
  sgn = ''
  piS = math.prod(S)
  for n in range(1, piS):
    if n%piS + (n*n -n)%piS >= piS:
      QS.append(n) 
  if parity(S) < 0:
    sgn = '-'
  else:
    if parity(S) > 0:
      sgn = '+'
    else:
      sgn = '0'
  print("{0}: {1}".format(len(QS)/piS, sgn))
#  print(-parity(S)*piS)
#  print(QS)
#  print(S)

#SSP



[[p, [S for S in qual2(N, N-1) if min(S) == p]] for p in primes if p < N]

[[p, sum([parity(S) for S in qual2(N, N-1) if min(S) == p])] for p in primes if p < N]

[p for p in primes if p < N and sum([parity(S) for S in qual2(N, N-1) if min(S) == p]) > 1]

#N=150


[N for N in range(5, 2000) if sum([parity(S) for S in qual2(N, N-1) if max(S) <= N//2]) > 0]



QQN = [S for S in QQ if [Q for Q in QQ if [p for p in Q if p not in S] == [] and math.prod(Q) < N] == []]
QQM = [S for S in QQ if S not in QQN]



PP = [P for P in comb(quals(20), 2) if abs(len(P[0]) - len(P[1])) == 1 and [p for p in P[0] if p not in P[1]] == [] or [p for p in P[1] if p not in P[0]] == []]
PP = [P for P in comb(quals(20), 2) if (len(P[0]) + len(P[1]))%2 == 1 and [p for p in P[0] if p not in P[1]] == [] or [p for p in P[1] if p not in P[0]] == []]

PP = [P for P in comb(quals(20), 2) if (len(P[0]) + len(P[1]))%2 == 1 and ([p for p in P[0] if p not in P[1]] == [] or [p for p in P[1] if p not in P[0]] == [] or [p for p in P[0] if p in P[1]] == [])]



maxlen = 0
solutions = []
def extend(start, covered, selections):
  global maxlen
  global solutions 
  if start >= len(PP):
    solutions.append(selections)
    return
  for P in PP[start:]:
    if P[0] not in covered and P[1] not in covered:
      coveredCopy = covered.copy()
      coveredCopy.append(P[0])
      coveredCopy.append(P[1])
      selectionsCopy = selections.copy()
      selectionsCopy.append(P)
      if len(selectionsCopy) >= maxlen:
        maxlen = len(selectionsCopy)
      extend(1 + PP.index(P), coveredCopy, selectionsCopy)


# identify whether S qualifies N based on N%pi(S)
[[m, [n for n in range(m+1,m*m) if m + (m*m-m)%n >= n and isSquareFree(n)]] for m in range(2, 20)]


# minimal-and-maximal qualifying sets
for N in range(2, 100):
  Q = quals(N)
  QMM = [S for S in Q if [T for T in Q if T != S and [x for x in T if x not in S] == []] == [] and [T for T in Q if T != S and [x for x in S if x not in T] == []] == []]
  if QMM != []:
    print("{0}: {1}".format(N, QMM))


# construct (maximal ?) collection of nested pairs differing in length by one
def nestedPairsNQ(N, Q):
  Q = quals2(N)
  QQ = sorted(sorted(Q, key = lambda s: sum(s), reverse = True), key = lambda s: len(s), reverse = True)
  QQD = {i : [S for S in QQ if len(S) == i] for i in reversed(range(1+len(QQ[0])))}
  QQU = []
  QQQ = []
  for S in QQ:
    if S not in QQU:
      for T in QQD[len(S)-1]:
        if T not in QQU:
          if [x for x in T if x not in S] == []:
            QQQ.append([S, T])
            QQU.append(S)
            QQU.append(T)
            break
  QQR = [S for S in QQ if S not in QQU]
  return {'nestedPairs': QQQ, 'remainder': QQR}

def nestedPairs(N):
  return nestedPairsNQ(N, quals(N))



QUALS{L}{M|P}{K}: K-th interval of length L*N below|above N*N
ex: QUALSM2[N] = qualD(N*(N-2), N*(N-1))
if M|P is ommitted it will be M and L will be 1.
if K is ommitted it will be 1.

