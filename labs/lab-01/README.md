# LAB 1 - Exploring data with numpy

In this lab we'll start exploring data with numpy. 
At the end of the lab you'll know

* How to load data as numpy arrays
* How to create new arrays
* How to perform arithmic operations on arrays
* How to slice arrays

Let's start by setting up your development environment for Python.

## Step 1: Install Visual Studio Code

We're going to use the python extension in VSCode to make all of our python code.
You can download it from https://code.visualstudio.com.

Please follow the on-screen instructions to install this tool. 

After installing VSCode, install the python addon. Click on the addons icon
in the side-bar and search for python. Next, click the install button on the 
add-on details page to install the Python addon.

Once you've install VSCode, you're ready to get started with the lab.
In the next step we'll create our first python notebook.

## Step 2: Create a new notebook

Open the root folder of the course `ml-quickstart-guide` in VSCode. 
Once you've opened the folder, expand the treeview until you see the folder
`labs/lab-01/starter`. 

In the `starter` folder create a new file called `numpy.ipynb`. This is the file
we're going to use for exploring numpy.

You should get an editor window similar to this:

![Editor window](media/notebook-editor.png)

In this editor you can execute fragments of python interactively.
Notebooks are a useful tool when it comes to exploring data as they
allow you to execute code, visualize data, and document your work together in one place.

### Quick tips

* You can add a new cell by clicking the plus button on the toolbar.
* Each cell is of a certain type. Select a cell, press <kbd>Esc</kbd> and then <kbd>M</kbd> to convert a cell to markdown or <kbd>Y</kbd> to convert it to python.
* You can reorder cells by dragging them around.
* You can execute a cell by pressing <kbd>Ctrl</kbd> + <kbd>Enter</kbd>

## Step 3: Load the population data from disk

Before we can work with data we need to load some data from disk.
Numpy supports loading data as arrays as well as creating new arrays.

Import the numpy package using the following code:

``` python
import numpy as np
```

Use the function [numpy.load](https://numpy.org/doc/1.18/reference/generated/numpy.load.html?highlight=load#numpy.load) to load the file `../data/population.py` and store it in a variable `population`.

Now that we have the population data, we also need to load the
employment data from disk. This data is also stored as a numpy
array.

## Step 4: Load the employment data from disk

Using the same function as in the previous step, load the 
file `../data/employment.npy` into a variable `employment_rate`.

Once we've loaded the second dataset, we can start to do some interesting things with the data.

## Step 5: Explore the loaded arrays

The arrays that we've loaded contain data about the population for a set of countries and employment figures for the same countries.

The employment data is stored as percentages while the population
is stored as absolute numbers.

Let's figure out if we can get from a percentage to an absolute number of people that are unemployed per country.

To do this, we first need to make sure that we have the right shape
for what we're trying to do.

Use the [shape](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.shape.html?highlight=shape#numpy.ndarray.shape) property on both arrays to figure out the dimensions
of the datasets. Make sure that the shapes are the same

Next, make sure that the data has the right type by checking the 
[dtype](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.dtype.html?highlight=dtype#numpy.ndarray.dtype) property.

## Step 6: Calculate the absolute number of people that are unemployed

In the previous step we've made sure that we have the right type and shape of data. Now it's time to convert the percentage of unemployed people to an absolute number.

Print the first ten rows of the `employment_rate` array using
a combination of array slicing and the `print` function.

You'll notice that the employment rate is stored as a value 
between 0 and 100. It's a percentage. 

Use this knowledge to calculate the absolute number of 
people employed using the `population` array and the `employment_rate` array.

Store the result of the calculation in the variable `absolute_employment`.

Now that you've done the maths, let's combine the results into
a single array.

## Step 7 Combine the array into a single array

First, create a new array using the [numpy.empty](https://numpy.org/doc/1.18/reference/generated/numpy.empty.html?highlight=empty#numpy.empty) function. Make sure the empty array has the same number of rows as the other arrays and 3 columns (one for each series).


Assign the values from the population array
to the first column in the newly created array.

Then, assign the values from the `employment_rate` array
to the second column.

Finally, assign the values from the `absolute_employment` array
to the third column.