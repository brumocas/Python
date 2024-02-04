import tensorflow as tf


# Creating tensors 
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.5435, tf.float64)

print()
print(string)
print(number)
print(floating)
print()

# Tensors Rank/Deegre of Tensors
rank1_tensor = tf.Variable(["Test"], tf.string) # List
rank2_tensor = tf.Variable([["test","ok"],["test","yes"]], tf.string) # Matrix

print(rank1_tensor)
print(rank2_tensor)
print()

# Determining the rank of a Tensor
print(tf.rank(number))
print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor))
print()

# Shape of a tensor, tells us the number of elements per dimension
print(rank2_tensor.shape)
print()

# Changing tensors shape
tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1, [2,3,1])
print(tensor2)
tensor3 = tf.reshape(tensor2, [3, -1]) # Reshapes with the ranks lefts to be filled
print(tensor3)
print()

# Different types of tensor
# Variable -> muttable
# Constant -> immuttable, but can be copied 
# PlaceHolder -> immuttable, but can be copied
# SparseTensor-> immuttable, but can be copied







