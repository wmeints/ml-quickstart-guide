# HOUR 5 

Machine learning with scikit-learn

---

## Steps for building a machine learning model

- Prepare a dataset
- Select and train a model
- Validate the trained model

---

## What is scikit-learn?

* A machine learning library
* Contains tools for all of the steps mentioned
* Works great with pandas and numpy

---

## How does scikit-learn work?

There are 3 important parts to the framework:

* Transformers/preprocessors
* Estimators
* Model evaluation logic

---~

## How does scikit-learn work?

In addition to this there are:

* Pipelines
* Automatic model searches

---~

### Transformers in scikit-learn

``` python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.random.random((20, 5))
scaler = StandardScaler()

scaler.fit(X)
X_scaled = scaler.transform(X)
```

Useful documentation:
<small>https://scikit-learn.org/stable/modules/preprocessing.html</small>
<small>https://scikit-learn.org/stable/modules/impute.html</small>
<small>https://scikit-learn.org/stable/modules/preprocessing_targets.html</small>

<!-- .element: class="fragment" -->

---~

### Estimators in scikit-learn

``` python
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier()

model = classifier.fit(X_train,y_train)
y_predicted = model.predict(X_test) # or use transform
```

Useful documentation:
<small>https://scikit-learn.org/stable/supervised_learning.html</small>
<small>https://scikit-learn.org/stable/unsupervised_learning.html</small>

<!-- .element: class="fragment" -->

---~

### Validating models in scikit-learn

``` python
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, f1_score, ...
```

Useful documentation: 
<small>https://scikit-learn.org/stable/modules/model_evaluation.html</small>

<!-- .element: class="fragment" -->

---

## Putting it all together

Let's take a look at how you can build a machine learning model with
scikit-learn in a python notebook.

---~

## Case for this module

Predict **life expectancy** based on

* Emissions
* Income per person
* Employment rate

<small>https://www.gapminder.org/data/</small>

---~

### Steps in the demo

* First, we'll load the data
* Next, we'll preprocess the data
* Then, we'll train a model
* Finally, we'll evaluate the model using metrics

---~

# Let's dive in!