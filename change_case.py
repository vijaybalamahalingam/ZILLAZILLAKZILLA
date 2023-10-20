s=input("Enter the Sentence for case to be changed: ")
def swap_case(st):
  s=""
  x=len(st)
  for i in range(x):
    y=st[i]
    if(y.isupper()):
      s=s+y.lower()
    elif(y.islower()):
      s=s+y.upper()
    else:
      s=s+y
  return s
result=swap_case(s)
print(result)