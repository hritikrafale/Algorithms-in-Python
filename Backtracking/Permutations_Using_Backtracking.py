
#permute function
def permute(arr,n,i):
	if(i==n):
		print("\n")
		for k in range(0,n):
			print(arr[k],end=" ")
		return 1
	else:
		for j in range(i-1,n):
			arr[i-1],arr[j]=arr[j],arr[i-1]
			i=i+1
			check=permute(arr,n,i)
			i=i-1
			arr[i-1],arr[j]=arr[j],arr[i-1]		





#main function

arr=['a','2']
n=2
permute(arr,n,1)