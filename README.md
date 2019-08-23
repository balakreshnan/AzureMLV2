# AzureMLV2

Azure machine learning service - Low Code Machine Learning

## Introductions

The purpose of this lab is to build end-to-end a ML solution for solving a sales operation use case. This lab closes the gap between data science and DevOps. The ‘model’ developer can now deploy and see how the model is consumed by other downstream systems – thereby providing several simplifications in the data processing. Not all use cases in the data science domain are going to be like this fully automated one.  This lab will also use a visual tool to build models in an easy to deploy manner and will cover the main steps of a data science life cycle process.

## Pre-Requiste

Azure Account ($200 account or Enterprise account).  The Enterprise account needs a resource group with Owner access. All resources to be used throughout this tutorial need to be registered in the subscription.

## Resources used in the Lab

- Machine Learning Service Workspace
- Container Registry
- Application Insights
- Key Vault
- Storage Account – Blob Storage
- Azure Kubernetes Service (AKS)

    - Kubectl is also needed to look at the Kubernetes Dashboard
    - https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-windows
- Batch AI workspace
- PostMan or Advanced REST Client for Chrome browser

To create the above resource, the Azure subscription needs to have enough permissions. This requirement should be verified with the corresponding IT/Cloud resource manager.

Batch AI workspace is used for model building and development. AKS and cluster is used for model deployment and consumption purposes. The Batch is required for AKS level development .  AKS must run all the time since it deploys REST API to consume the model output.

## Use Case

A simple regression model will be used to estimate a Contoso AI sales operation usage. The Contoso data set has year, month and consumption data which represents the sales operation spends. The data and the company name are fictious. The idea here is to predict the operation cost for sales operation. 

## Architecture

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/AMLStudioV2Architecture.jpg "Architecture")

## Architecture Process

- Development
- Deployment

### Development Process

The development process for data science is different from regular computer science or software engineering modeling process. There is constant feedback into the machine learning model to make the model better over time. For development, there is a need to execute a thorough inspection of the data to wrangle and adjust the data set prior to running it through the model training process. Although data wrangling might be a time-consuming process, this is an invaluable step that simplifies model management. This process introduces a good degree of hands on and discovery.  For example, it is important to make sure that the data set contains the features in the correct format. This is a discovery process that must be executed early for any use case.

Most of the data science time/effort is used on data wrangling, especially in setting and configuring the blend of features.  Also, when modelling depends on ensembled models or straight forward modelling, time consumed is also a factor. Moreover, running multiple algorithms against the data can also become a time-consuming task. 

Another area of development is the model and algorithmic cross validation which is intended to avoid overfitting and/or underfitting the model. The data engineer must consider this aspect in the scrum planning.

The above process goes through iterations with different features. Therefore, the need for compute capacity is very necessary in the development process, which is different from regular software life cycles. In Software Engineering, a lower level of compute resources is required to develop a solution. In the Data Science, enough compute capacity and scalability on demand are very important requirements. Moreover, Azure DevOps provides the ability to maintain version control in the Data Science development process.

### Deployment Process

This process follows similar paradigm as in the development process. The model output is more of “brain file” which is in binary format. This brain file (aka ‘model’) is used for scoring the features and it is to be executed in real time. The footprint of the brain file is small in comparison with the training-phase data volumes. To score the data a smaller set of compute resources is needed. One industry accepted mechanism to make the model available is to containerize the model as a docker container and to deploy it either in AKS or an edge runtime appliance with Kubernetes or Docker processes in it.  For now, only Linux-based containers are available, but this might change in future. Also, the ability to automate the deployment process using Azure DevOps is also available.

## Technology Choice

### Open Source and First Party

Technology choice for Architecture was based on agility in programming and agility in compute and agility in deployment. Languages like Python, R or .NET can be used.  For compute, options like Machine Learning Compute, Azure Databricks, HDInsight’s, or Data Lake Analytics can be used. For deployment container platforms, AKS is the primary candidate but Azure container instances are also available.

Although there are myriad advantages on open source, there is also lack of support for it. The biggest challenges are versioning and library dependencies around the packages that can be used. Even though the deployment can be scripted, there are issues with maintaining so many different versions of packages.

Preferably using Platform as a Service is recommended - Using PaaS allows us to scale when needed.

## Prepare Dataset

Download the data set from a specific location or a data set can be provided on request. Sample data set is available for download from GitHub.

## Understand dataset

Look at the data and see how to move forward. A data set has features and not all features might be relevant. For example, the Contoso set has year, month and consumption (in thousands). The data is aggregated data for sales operation over close to 2 and half year. The Data is made up data and was not copied from anywhere. Look and see dollars spent every month on operations from sales department. You can also use your own dataset, if desired. The data set chosen for this lab is very simple and available in any enterprise scenario. In the real work, the data set might be complex and might need subject-matter expertise to explain what these features means.

## Lab Starts here.

https://github.com/balakreshnan/AzureMLV2/blob/master/lab/Automllab.md
