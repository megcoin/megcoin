import hashlib, binascii

t='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def numtowif(numpriv):
 # for bitcoin (80=128)
 # for testcoin (EF==239 == testnet)
 step1 = 'EF'+hex(numpriv)[2:].strip('L').zfill(64)
 step2 = hashlib.sha256(binascii.unhexlify(step1)).hexdigest()
 step3 = hashlib.sha256(binascii.unhexlify(step2)).hexdigest()
 step4 = int(step1 + step3[:8] , 16)
 return ''.join([t[step4/(58**l)%58] for l in range(100)])[::-1].lstrip('1')

def wiftonum(wifpriv):
 return sum([t.index(wifpriv[::-1][l])*(58**l) for l in range(len(wifpriv))])/(2**32)%(2**256)

def validwif(wifpriv):
 return numtowif(wiftonum(wifpriv))==wifpriv

def pubtoaddr(numpub):
 pubkey1=hex(numpub)[2:].strip('L').zfill(130)
 #print pubkey1
 pubkey2=hashlib.sha256(binascii.unhexlify(pubkey1)).hexdigest()
 #print pubkey2
 pubkey3=hashlib.new('ripemd160',binascii.unhexlify(pubkey2)).hexdigest()
 #print pubkey3
 # for bitcoin (0)
 #pubkey3b='00'+pubkey3
 # for testcoin (111)
 pubkey3b='75'+pubkey3
 #print pubkey3b
 pubkey4=hashlib.sha256(binascii.unhexlify(pubkey3b)).hexdigest()
 #pubkey4=hashlib.sha256(binascii.unhexlify(pubkey3b)).hexdigest()
 #print pubkey4
 pubkey5=hashlib.sha256(binascii.unhexlify(pubkey4)).hexdigest()
 #print pubkey5
 pubkey5a=pubkey5[:8]
 #print pubkey5a
 pubkey6=pubkey3b+pubkey5a
 #print pubkey6
 #print pubkey6[:2]
 pubnum=int(pubkey6,16)
 #print pubnum
 pubnumlist=[]
 while pubnum!=0: pubnumlist.append(pubnum%58); pubnum/=58
 address=''
 for l in ['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'[x] for x in pubnumlist]:
  address=l+address
 if pubkey6[:2]=='00':
  address='1'+address
 return address

print "wallet import format"
print numtowif(0x5e4a8229e81a434b0646dcdbeb4b03083e2bd05af26fcf2e4e4aa37eacb2913b)
print "wallet public address"
print pubtoaddr(0x04580e17442b4465fbf1eb8a039855343739f69f83222c3c6590c219dcd2d883bff96ebf6198ddb9a75baffffbc1be62f05261d7dfec58d8a06cf3809c6cefe620)
