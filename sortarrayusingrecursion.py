n =int(input())
l = list(map(int, input().split()))

def inserti(l, p):
  if len(l)==0 or l[-1]<=p:
    l.append(p)
    return
  v = l.pop()
  inserti(l,p)
  l.append(v)
  return 

  
def sorti(l):
  if len(l)==1:
    return
  p = l.pop()
  sorti(l)
  inserti(l,p)
  return 
 
print(l)
sorti(l)

print(l)