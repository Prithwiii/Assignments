# -*- coding: utf-8 -*-
"""lab 5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zd4hr-zZdefGzWZsLnBa40N6Uoeyo5J5
"""

N, S= map(int, input().split())
list1= list(map(int, input().split()))
flag=False
left,right=0 , N-1
while left<right:
  sum= list1[left]+list1[right]
  if sum==S:
    print(left+1, right+1)
    flag=True
    break

  elif sum<S:
    left+=1
  elif sum>S:
    right-=1
if flag==False:
 print(-1)

N= int(input())
alice=list(map(int,input().split()))
M=int(input())
bob=list(map(int, input().split()))
final=[]
i,j=0,0
while i<N and j<M:
  if alice[i]<bob[j]:
    final.append(str(alice[i]))
    i+=1
  else:
    final.append(str(bob[j]))
    j+=1
while i<N:
  final.append(str(alice[i]))
  i+=1
while j<M:
  final.append(str(bob[j]))
  j+=1
print(" ".join(final))

N, K = map(int, input().split())
arr1= list(map(int,input().split()))
i,j= 0,0
curr_sum=0
flag=False
max_length=0
while i<N :
  curr_sum+=arr1[i]
  while curr_sum>K and j<i:
    curr_sum-=arr1[j]
    j+=1
   if curr_sum<=K:
    # 0 1 2 3
  #                                                             1 2 6 4           i j
  #                                                                                0 0

  #                                                                                 curr=1
  #                                                                                 1 0
  #                                                                                 2 0\
  #                                                                                 curr= 3
  #                                                                                 3 0
  #                                                                                 curr=9
  #                                                                                 ekhon curr er loop e dhukbe
  #                                                                                 cause curr>k
  #                                                                                  j<i
  #                                                                                  curr=8
  #                                                                                  3 1
  #                                                                                  loop e dhukbe na karon curr not bigger than k
  #                                                                                  ber hoye dkhbe shoman
  #                                                                                  current length= 3-2
  #                                                                                  1 +1=2


  #                                                             k=8

    current_length=i-j+1
    max_length=max(max_length,current_length)

    flag= True


  i+=1
if not flag:
  print("0")
else:
  print(max_length)

a,b= map(int,input().split())
arr1= input().split()


for i in range(b):
         x,y= map(int,input().split())
         l=0
         r=len(arr1)

         while l<r:
             mid=(l+r)//2

             if int(arr1[mid])<x:
                l=mid+1
             else:
                 r= mid
         left=l
         l=0
         r=len(arr1)
         while l<r:
            mid=(l+r)//2
            if int(arr1[mid])<=y:
              l=mid+1
            else:
              r=mid
         right=l
         print(right-left)

T=int(input())

    for i in range(T):
      S=input()
      l=0
      right=len(S)-1
      flag=False
      first=-1
      while l<=right:
        mid=(l+right)//2
        if S[mid]=="1":
          first=mid+1

          right=mid-1
        else:
          l=mid+1
      print(first)