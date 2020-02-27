# HOUR 9

Introduction to running experiments with Azure Machine Learning Service

---

## What is Azure Machine Learning Service

---~

<img src="media/azureml.webp" class="plain">

---~

### What you'll be using today

* Datasets
* Experiments
* Deployment

---

## Getting started

Let's set up a workspace for our experiments

---~

### Steps

1. Create a workspace
2. Download the access tokens
3. Connect to the workspace

---

## Running an experiment locally

---~

### Steps

1. Install the azureml sdk
2. Upgrade your project to run inside an experiment

---

## Recording data

Let's record some data about our experiment

---~

### Recording metrics

---~

### Tips and tricks for recording metrics

* Don't go overboard recording metrics
* Record stuff that you want to compare later

---~

### Recording outputs

How to store models in the model registry after training.

---

## Managing the data for your experiments

---~

### Steps

1. Upload data to blob storage
2. Register the dataset in your workspace
3. Use the dataset in your ML project

---

## Running experiments on a dedicated environment

Sometimes your own computer doesn't quite cut it.

---~

### Options for training

* Local
* A dedicated compute instance
* A training cluster

---~

### Setting up a training cluster

1. Create the compute instance in the portal
2. Running your experiment against the compute cluster