#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a = np.array([1,2,3])
print(a)


# In[3]:


# more than one dimension
import numpy as np
a = np.array([[1,2],[3,4]])
print(a)


# In[6]:


# minimum dimensions
import numpy as np
a = np.array([1,2,3,4,5], ndmin=2)
print(a)


# In[7]:


# dtype parameter
import numpy as np
a = np.array([1,2,3], dtype=complex)
print(a)


# In[8]:


# using array-scalar type
import numpy as np
dt = np.dtype(np.int32)
print(dt)


# In[9]:


# int8, int16, int32, int 64 can be replaced by equivalent string 'i1', '12', '14', etc.
import numpy as np
dt = np.dtype('i2')
print(dt)


# In[10]:


# using endian notation
import numpy as np
dt = np.dtype('>i2')
print(dt)


# In[11]:


# first create structured data type
import numpy as np
dt = np.dtype([('age', np.int8)])
print(dt)


# In[13]:


# now apply it to ndarray object
import numpy as np
dt = np.dtype([('age', np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a)


# In[15]:


# file name can be used to access content of age column
import numpy as np
dt = np.dtype([('age', np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a['age'])


# In[21]:


# structured data type called student
import numpy as np
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)


# In[22]:


# applying value
import numpy as np
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
values = np.array([('Anandu', 18, 67), ('Dhanya', 20, 70)], dtype=student)
print(values)


# In[24]:


# ndarray.shape
import numpy as np
a = np.array([[1,2,3], [4,5,6]])
print(a.shape)


# In[26]:


# this resizes the ndarray
import numpy as np
a = np.array([[1,2,3], [4,5,6]])
a.shape = (3,2)
print(a)


# In[30]:


# reshape()
import numpy as np
a = np.array([[1,2], [3,4], [5,6]])
b = a.reshape(2,3)
print(b)


# In[31]:


# arange()
import numpy as np
a = np.arange(24)
print(a)


# In[34]:


# reshape
import numpy as np
a = np.arange(24)
a.ndim
b = a.reshape(2,4,3)
print(b)


# In[35]:


# dtype of array is int8 (1 byte)
import numpy as np
x = np.array([1,2,3,4,5], dtype=np.int8)
print(x.itemsize)


# In[36]:


# dtype of array is float32 (4 bytes)
import numpy as np
x = np.array([1,2,3,4,5], dtype=np.float32)
print(x.itemsize)


# In[37]:


# current values of flags
import numpy as np
x = np.array([1,2,3,4,5])
print(x.flags)


# In[40]:


# empty()
import numpy as np
c = np.empty([3,2], dtype=int)
print(c)


# In[41]:


# zeros() default type is float
import numpy as np
x = np.zeros(5)
print(x)


# In[45]:


import numpy as np
x = np.zeros((2,2), dtype=[('x','i4'), ('y', 'i4')])
print(x)


# In[46]:


import numpy as np
x = np.zeros((2,2), dtype=int)
print(x)


# In[47]:


# array of five ones default type is float
import numpy as np
x = np.ones(5)
print(x)


# In[48]:


import numpy as np
x = np.ones([2,2], dtype=int)
print(x)


# In[49]:


# convert list to ndarray
import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)


# In[50]:


import numpy as np
x = [1,2,3]
a = np.asarray(x, dtype=float)
print(a)


# In[51]:


# tuple to ndarray
import numpy as np
x = (1,2,3)
a = np.asarray(x)
print(a)


# In[53]:


# ndarray from list of tuples
import numpy as np
x = [(1,2,3), (4,5)]
a = np.asarray(x)
print(a)


# In[55]:


# arange
# start and stop parameters set
import numpy as np
x = np.arange(10,20,2,dtype=float)
print(x)


# In[56]:


# linspace -   numpy.linspace(start,stop,num,endpoint,retstep,dtype)
import numpy as np
a = np.linspace(2.0, 3.0, num=5)
print(a)
b = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(b)
c = np.linspace(2.0, 3.0, num=5, retstep=True)
print(c)



# In[58]:


# logspace -    numpy.logspace(start,stop,num,endpoint,base,dtype)
import numpy as np
a = np.logspace(2.0, 3.0, num=5)
print(a)
b = np.logspace(2.0, 3.0, num=5, endpoint=False)
print(b)
c = np.logspace(2.0, 3.0, num=5, base=2.0)
print(c)


# In[ ]:




