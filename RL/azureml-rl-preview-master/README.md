
# Azure Machine Learning - Reinforcement Learning Preview

<!-- 
Guidelines on README format: https://review.docs.microsoft.com/help/onboard/admin/samples/concepts/readme-template?branch=master

Guidance on onboarding samples to docs.microsoft.com/samples: https://review.docs.microsoft.com/help/onboard/admin/samples/process/onboarding?branch=master

Taxonomies for products and languages: https://review.docs.microsoft.com/new-hope/information-architecture/metadata/taxonomies?branch=master
-->

This is an introduction to the [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/service/) private preview for Reinforcement Learning using the [Ray](https://github.com/ray-project/ray/) framework.

Using these samples, you will be able to do the following.

1. Create an Azure ML workspace and computing clusters for running Ray.
2. Run some experiments training a reinforcement learning agent using Ray and rllib.

## Contents

Outline the file contents of the repository. It helps users navigate the codebase, build configuration and any related assets.

| File/folder       | Description                                |
|-------------------|--------------------------------------------|
| `files`           |  Script and configuration files.                       |
| `.gitignore`      | Define what to ignore at commit time.      |
| `CONTRIBUTING.md` | Guidelines for contributing to the sample. |
| `README.md`       | This README file.                          |
| `LICENSE`         | The license for the sample.                |
| `Workspace Setup.ipynb` | Notebook to setup workspace for Azure ML RL |
| `Ray Pong.ipynb`  | Sample notebook to train Pong agent using Ray without Rllib   |
| `Rllib Pong.ipynb` | Sample notebook to train Pong agent using Rllib with Python script. |
| `Rllib Atari.ipynb` | Sample notebook to train Atari agents using Rllib with YAML configuration. |

## Prerequisites

To make use of these samples, you need the following.

* Microsoft Azure subscription
* A Microsoft Azure resource group in one of the following regions: `eastus` or `westcentral` or `westeurope` or `southcentralus`.
* A virtual network set up in the resource group.
  * The `Workspace setup` notebook shows you how to create a virtual network.  Or you can use an existing one.
* An Azure Machine Learning Workspace in the resource group above.
  * Make sure to create the workspace in the same region as the resource group above.
    * The `Workspace setup` notebook shows you how to create a workspace from the network.

## Setup

You can run these samples in the following ways.

* On a Azure ML Notebook VM.
* On a workstation with Python and the Azure ML Python SDK installed.

### Azure ML Notebook VM

#### New Notebook VM

If you have a notebook VM created starting in December 2019, then the reinforcement learning SDK is already installed.  You can start using the sample notebooks right away.

#### Update Notebook VM

If you have a notebook VM created before December 2019, then update it and install the RL SDK using the following commands in a notebook cell.

```shell
# We recommend updating pip to the latest version.
!pip install --upgrade pip
# Update Azure ML SDK to the latest version
!pip install --upgrade azureml-sdk
# For Jupyter notebook widget used in samples
!pip install --upgrade azureml-widgets
# For Tensorboard integrated used in samples
!pip install --upgrade azureml-tensorboard
# Install Azure ML RL SDK
!pip install --upgrade azureml-contrib-reinforcementlearning
```

### Your own workstation

For a local workstation, create a Python environment and [install Azure ML SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/install?view=azure-ml-py) and the RL SDK. We recommend Python 3.6 and higher.

```shell
# Activate your environment first.
# e.g.,
# conda activate amlrl
# We recommend updating pip to the latest version.
pip install --upgrade pip
# Update Azure ML SDK to the latest version
pip install --upgrade azureml-sdk
# For Jupyter notebook widget used in samples
pip install --upgrade azureml-widgets
# For Tensorboard integrated used in samples
pip install --upgrade azureml-tensorboard
# Install Azure ML RL SDK.
pip install --upgrade azureml-contrib-reinforcementlearning
# To use the notebook widget, you may need to register and enable the Azure ML extensions first.
jupyter nbextension install --py --user azureml.widgets
jupyter nbextension enable --py --user azureml.widgets
```

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
