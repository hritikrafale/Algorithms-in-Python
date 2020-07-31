#function subsets to generate subsets
def subsets(arr,N,i):
	if(i==N):
		print("\n")	
		for k in range(0,N):
			if(arr[k]!=0):
				print(arr[k],end=" ")	
		return 1
	else:
		for  j in range(0,2):
			if(j!=0):
				temp=arr[i]
				arr[i]=0
			i=i+1
			subsets(arr,N,i)
			i=i-1
			if(j!=0):
				arr[i]=temp



#main function
arr=[4,3,2,1]
N=4
i=0
subsets(arr,N,i)