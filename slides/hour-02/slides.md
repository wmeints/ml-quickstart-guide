# HOUR 2

Doing maths with numpy

---

## What is numpy and why should you care?

---~

### Numpy is a numeric library for python

- Helps expressing matrices and vectors <!-- .element: class="fragment" -->
- Highly optimized for performance <!-- .element: class="fragment" -->
- Machine learning requires both <!-- .element: class="fragment" -->

---~

# Basis for everything in numpy 

<img src="media/numpy-arrays.png" class="plain">

---

## Getting access to numpy

```
pip install numpy
```

Anaconda includes numpy by default, so you don't have to install it.

---

## Working with arrays

---~

### Loading the numpy package

```
import numpy as np
```

---~

### Creating a new array

```
np.zeros((3,4))         # 3x4 array with zeros
np.ones((2,2))          # 2x2 array with ones
np.array([1,2,3,4])     # convert list to a 1-d array
np.random.random((2,2)) # create a 2x2 array with random values
```

---~

### Inspecting arrays

```
my_array.shape  # shape of the array
my_array.ndim   # number of dimensions
my_array.size   # number of elements in the array
my_array.nbytes # number of bytes stored in the array
```

---~

### Array length?

```
my_array.size # size of the array
len(my_array) # length of the array
```

Can you tell the difference?

---

## Broadcasting

An important concept that makes calculations with arrays possible.

---~

### When can you broadcast?

If the dimensions are equal

```
array_1 = np.random.random((2,2))
array_2 = np.random.random((2,2))

array_1 * array_2
```

---~

### When can you broadcast?

If one of the arrays is 1-dimensional i.e. a vector

```
array_1 = np.random.random((2,2))
array_2 = np.random.random(2)

array_1 + array_2
```

---~

### Can you broadcast this?

```
array_1 = np.random.random((3,4))
array_2 = np.random.random((2,5))

array_1 * array_2
```

You can't broadcast this, dimensions are not equal. <!-- .element: class="fragment" -->

---~

### Can you broadcast this?

```
array_1 = np.random.random((3,4))
array_2 = np.random.random((3,1,4))

array_1 * array_2
```

You can broad cast this, since one of the dimensions has a size of 1 <!-- .element: class="fragment" -->

---~

### Can you broadcast this?

```
array_1 = np.random.random((2,4))
array_2 = np.random.random((4,2))

array_1.T * array_2
```

You can broadcast these arrays, as the first one is transposed. <!-- .element: class="fragment" -->

---

### Array slicing

Looks similar to slicing lists in python.
Here's a few examples.

---~

### Slice a single dimension

```
my_array = np.random.random(4)
my_array[0:2]
```

```
my_array.shape # 2
```
<!-- .element: class="fragment" -->

---~

### Slice across multiple dimensions

```
my_array = np.random.random((4,8))
my_array[0:2, 4:8]
```

```
my_array.shape # (2,4)
```
<!-- .element: class="fragment" -->

---~

### Grab remaining dimensions

```
my_array = np.random.random((4,8,2))
my_array[0:2, ...]
```

```
my_array.shape # (2,8,2)
```
<!-- .element: class="fragment" -->

---

## Other interesting operations

```
my_array.mean()
my_array.median()
my_array.max()
```

---

## Documentation

https://numpy.org/