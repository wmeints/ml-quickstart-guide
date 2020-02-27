# HOUR 11

Deploying models to production with Azure Machine Learning Service

---

## Why should you be versioning your models?

Promotes tracability:

Experiment -> Run -> Model + Metrics -> Deployment

---

## Registering models in the model registry

1. Record the output in your experiment
2. Register the model

---

## Deployment options for Azure Machine Learning Service

* Azure Container Instance (dev + test, small-scale production)
* Kubernetes cluster (large-scale production)

---

## Deploying to Azure Container Instances

1. Create a deployment configuration
2. Execute a deployment from python
