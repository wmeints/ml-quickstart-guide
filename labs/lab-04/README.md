# LAB 4 - Running your project as an experiment in Azure Machine Learning Service

In this lab we'll explore how to use Azure Machine Learning Service to run experiments.
We'll cover the following topics:

- Setting up a machine learning workspace
- Setting up your project
- Creating a dataset
- Setting up a compute environment
- Running an experiment

## Setting up a machine learning workspace

To run machine learning experiments on Azure you'll need to create a machine
learning workspace. Creating a machine learning workspace is performed in
two steps:

- Creating a new resource group
- Creating a new workspace

Let's start with a new resource group

### Creating a new resource group

The resource group will contain the workspace resources. Follow these
steps to create the resource group:

- Navigate to https://portal.azure.com/ login with your account
- Click the `+` button on the homepage.

![Homepage](media/azure-portal.png)

- Next, search for `resource group` and press <kbd>ENTER</kbd>.
- Select the `Resource Group` item from the list and click `Create`.

![Resource group wizard](media/new-resource-group.png)

- Enter a name for the resource group
- Choose `West Europe` as the region for the group
- Then, Click `review + create` to go to the final step of the wizard
- Finally, Click `Create` to create the resource group

### Creating a new workspace

Once the resource group is created, it's time to create the workspace.
Follow these steps to create the workspace:

- Navigate to the resource group you just created.
- Next, click the `Add` button to create a new resource.

![Resource group details](media/resource-group-details.png)

- Then, search for `machine learning` and select `Machine learning` from the dropdown.
- Next, click `Create`

![Create workspace](media/create-workspace.png)

- Use the following details to create the workspace

  - Workspace Name: Choose a unique name
  - Region: West Europe
  - Workspace edition: Basic

- Click `Review + Create`
- Click `Create`

It will take a few minutes for the workspace to be fully operational.

### Installing the Azure ML SDK

Once you've got a workspace, you can prepare your computer for working with
the workspace. Follow these steps to prepare your computer:

- Open an Anaconda prompt
- Execute the command `pip install azureml-sdk`

## Setting up your project

There's numerous ways in which you can set up a project for use with 
Azure Machine Service. We're going to use another cookiecutter template,
that's specifically made for the purpose of running on Azure Machine Learning
Service.

Create a new project using the following command:

```
cookiecutter https://github.com/wmeints/azureml-cookiecutter
```

Cookiecutter will ask you for the following parameters:

- `project_dir`: The folder where to create the project, enter `autompg` as the value.
- `project_name`: The full name of the project, enter a descriptive name.
- `package_name`: The package name to create, enter `autompg` as the value.

After you've created the project, explore the README.rst file to get a sense
of what's included in the project.

## Creating a dataset

Once the workspace is ready, navigate to the `starter` folder and open it
in VSCode.

Next, navigate to the workspace on the Azure Portal (https://portal.azure.com).
Download the `config.json` file and save it in the root of your project folder.

After we've configured your project, we need to upload a dataset to the workspace.
For this you're going to need a dataset. You can find the dataset in 
[data/auto-mpg.csv](data/auto-mpg.csv). Copy this file to the `data/raw` folder in
your project.

In the project folder, you'll find a sub-folder `tasks` that contains a file
`make_dataset.py`. Execute the following command to upload your data to the workspace.

```
python tasks/make_dataset.py --name autompg --input_folder data/raw --output_folder autompg
```

The `make_dataset` task performs the following steps:

- It retrieves the workspace based on the `config.json` you created.
- Next, it determines the default data store for the workspace.
- Then, it uploads the data files from the input path to workspace.
- After, it creates a new dataset from the blob storage path.
- Finally, it registers the dataset.

When you've set up the dataset for your experiment, it's time to configure the
experiment itself.

**Note:** A lot of the work to create workspaces, datasets, etc. is done for you.
Feel free to explore the scripts in the `tasks` folder inside your project. You
may need to modify them in the future.

## Setting up a compute environment

The next step is to create a new compute environment for training the model.
The project that we generated contains a task `tasks/make_environment.py`.

Use the following command to execute the script:

```
python tasks/make_environment.py --name autompgtrain --vm_size Standard_D3_v2 --nodes 1
```

This will create a new environment for training the model. It will take a while
for the command to complete. 

After you've created the environment, continue to the next step, training the model.

## Running an experiment

Running an experiment in Azure Machine Learning Service can be done
in two ways:

- On your local machine
- On a remote compute target

We're going to explore how to run an experiment on a remote environment.
For this, we're going to have to modify `autompg/train.py`. 

Copy the following content to the `autompg/train.py` file:

```python
import joblib
from azureml.core import Run
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# The run is automatically determined.
# Use this to log data, get access to dataset, and publish your model.
run = Run.get_context()

# STEP 1: Get the datasets
################################################################################
# Datasets are made available in the input_datasets dictionary.

df_autompg = run.input_datasets['autompg'].to_pandas_dataframe()

X = df_autompg[['cylinders','displacement','horsepower','weight','acceleration']]
y = df_autompg['mpg']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# STEP 2: Preprocess the dataset
################################################################################
# Perform some last-minute transformations before training the model here.


# STEP 3: Train the model
################################################################################
# Train your model here. Please note, we're assuming scikit-learn in the 
# train_model task. If you plan to use Tensorflow, be sure to change the 
# estimator in the task as well. You can find more information here:
# https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-ml-models
# 
# Use run.log(), run.log_image(), run.log_table()
# or run.log_row() to log metrics as part of the run.
# You can learn more about logging here:
# https://docs.microsoft.com/en-us/azure/machine-learning/how-to-track-experiments

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

run.log('r_squared', score)

# STEP 4: Register the model
################################################################################
# First, store the model on disk by using joblib.dump('outputs/model.bin')
# then, call run.upload_file('model.bin', 'outputs/model.bin')
# after that, call run.register_model('model_name', 'model.bin')

joblib.dump(model, 'outputs/model.bin')

run.upload_file('model.bin', 'outputs/model.bin')
run.register_model('autompg', 'model.bin')
```

This script performs the following steps:

- It will retrieve the workspace based on the `config.json` in the project.
- Next, it will retrieve the dataset and preprocess it for training.
- Then, it will use the training set to train the model
- After that, it will validate the model and log the score
- Finally, it will save the model and register it in the workspace

Start training the model using the following command:

```
python tasks/train_model.py --experiment autompg --environment autompgtrain --dataset autompg
```

This command will run the experiment and log the results to the workspace.
You can view the results on https://ml.azure.com/
