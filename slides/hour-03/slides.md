# HOUR 3

Data wrangling with pandas

---

## What is pandas?

* Introduces the concept of a dataframe
* Used to work with tables that contain more than numbers
* Offers a wide range of operations to work with datasets

---

## What's a data frame?

<table>
    <thead>
        <th>Index</th>
        <th>Series</th>
        <th>Series</th>
    </thead>
    <tbody>
        <tr>
            <td>value</td>
            <td>value</td>
            <td>value</td>
        </tr>
        <tr>
            <td>value</td>
            <td>value</td>
            <td>value</td>
        </tr>
        <tr>
            <td>value</td>
            <td>value</td>
            <td>value</td>
        </tr>
        <tr>
            <td>value</td>
            <td>value</td>
            <td>value</td>
        </tr>
        <tr>
            <td>value</td>
            <td>value</td>
            <td>value</td>
        </tr>
    </tbody>
</table>

---~

### Column oriented

* Every column is stored as a Series (array)
* Data is stored as numpy arrays

---~

### An index is used

* To identify rows (a primary key if you will)

---

## Getting pandas

```
pip install pandas
```

Anaconda includes pandas by default, so you don't have to install it.

---

## Working with data frames

---~

### Importing pandas

``` python
import pandas as pd
```

---~

### Creating a data frame

```
my_array = np.random.random((2,2))
my_index = np.array(['row 1','row 2'])
column_names = np.array(['col 1', 'col 2'])

df = pd.DataFrame(data=my_array, index=my_index, columns=column_names)
```

```
          col 1     col 2
row 1  0.696469  0.286139
row 2  0.226851  0.551315
```
<!-- .element: class="fragment" -->

---~

### Creating a data frame

Usually though, you'll load data from disk.

```
df = pd.read_csv('filename.csv', sep=';')
df = pd.read_excel('filename.xlsx')
```

---

## Inspecting data frames

---~

### Getting information about the data frame

---~

### Summary statistics

---

## Slicing data frames

---~

### Selecting rows

---~

### Selecting columns

---~

### Slicing using boolean expressions

---

## Visualizing data frames

---~

### Plotting a bar chart

---~

### Plotting a histogram

---

## Other operations on data frames

