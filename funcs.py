import numpy as np

def check_partition(shape,size_block):
  if size_block.shape[0]!=2:
    print("Error! Size block should be of dim 2")
    raise ValueError 
  if shape[0]!=np.sum(size_block[0]) or shape[1]!=np.sum(size_block[1]):
    print("Error! Total block size should be equal to the shape")
    raise ValueError

# partition_A = 2 dim np array with lentgh of each block, [[lenght of columns],[lenght of rows]]
def tracy_sing(A,B,partition_A,partition_B):

# Check that the partition make sense
  try:
    check_partition(A.shape,partition_A)
    check_partition(B.shape,partition_B)
  except ValueError:
    print('Error!')
# Calculate the tracy-singh product
  prod=np.zeros(A.shape[1]*B.shape[1])
  for i in range(len(partition_A[0])):
    for k in range(len(partition_B[0])):
      # Here we start creating a new line
      newrow=np.zeros((partition_A[0][i]*partition_B[0][k],1))
      for j in range(len(partition_A[1])):
        for l in range(len(partition_B[1])):         
          sub_A = A[np.sum(partition_A[0][:i]):np.sum(partition_A[0][:i+1]),np.sum(partition_A[1][:j]):np.sum(partition_A[1][:j+1])]
          sub_B = B[np.sum(partition_B[0][:k]):np.sum(partition_B[0][:k+1]),np.sum(partition_B[1][:l]):np.sum(partition_B[1][:l+1])]

          sub=np.kron(sub_A,sub_B)
          newrow=np.hstack([newrow, sub])
      newrow=newrow[:,1:]
      prod = np.vstack([prod, newrow])

  return prod[1:,:]
