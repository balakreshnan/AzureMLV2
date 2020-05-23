# Architecture consideration for Machine/Deep Learning projects

## Machine/Deep learning application lifecycle management process

## Architecture

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/dlmlalm.jpg "ML/DL ALM process")


## Introductions

```
Note this article only applies to building machine learning or deep learning model from scratch or using existing model for transfer learning. 
```

So how does a machine learning application lifecycle process is goign to be. Given we know how the software application life cycle management works across different environment for dev, test, qa and production (the envirnment changes based on every organizations and their requirements). But how does Machine learning or Deep learning process works.

One thing to look is, in regular software engineering for development there is no need all the data and some times mocked up data is used for development of business logic. Can we do the same in machine learning and deep learning. For AI projects data is essential very key.

For AI which means machine learning, deep learning and reinforcement learning data is a key. Usually this data is only available in production system. Now as you see the development we need the production data. This can be the actual production or copy of production for even development.

Lets look at what are the major process in Machine/Deep learning projects.

1) Development of Model
2) Production Process for Retraining and Inferencing.

- Development of Model
    This is where we take all the data and develop a model based on use case. First it starts with defining the use case and accuracy to target to, and then source data sources for the data, DO data engineerng to get the data to usuable format by cleaning and doing other data operations. Then processed data set is split into train and test and validate and then model building is started. All the above process i described is done in iteration untill we get a satisfactory accuracy score from the model for that particular use case.
    All of the above is only to get the model built. Depending on the volume of data the computation can change. For example if the data set is only 10MB may be a virtual virtual machine with CPU/GPU depending on machine learning or Deep learning can be used for model building. Usually every developer would have their own development computation as sharing these compute at the same time becomes very slow and not productivtive at all.
    For scenario's with more than TB or large volumen GB or PB data then looking at Parallel Batch processing or Parallel framework like Spark to do the heavy lifting computation. Yes there will be some limitation based on what librarries you are using and what sdk's. For Example if Mllib is used spark has native support. Some time Azure Batch like services can be used to parallize the python based machine learning libraries.

- Production Process for Retraining and Inferencing.
    1) Inferencing
        Now once the model is satisfactory based on the use case requirement it is time to convert the model file or brain file or binary stored weights. Usually this is saves as pickle file for python or tensorflow pb file or graph or for keras h5 file. This file is very less in size compared to the data set. But depening on the use case the model size can vary, for example can go from few mb's to few gb's.
        Once the model is saved as binary brain file (remember there is no data saved here) is then used to built what is called inferencing code. Inferencing code is nothing but loading the saved model file and format the input data coming in to the right format for model and pass the input to model and predict the output value. Then output is formatted to send this back to client. For Example most inferencing is done using rest api using flask or .NET etc. So to develop the REST API we need to pass input as JSON formatted or keyvalue based data has to be processed. Not only that if the input data is not in the format expected by model then data engineering steps to make sure data set is prepared to be executed with model. Other wise the model is error out. Proper coding has to be in place to handle error handling and model versioning and also scoring performance stored and maintained to improve performance.
        Once the inferencing code is ready, well tested and then it is created as docker container. So define the docker image configuration with parameters and create the image and store in a container registery with proper versioning. 
        As the image is ready then it can be deployed any container based orchestration infrastructure or platforms. 
        Creating docker file and creating image and deploying into container registry and also deploying to container platform for api can all be automated usign DevOps practices using CI/CD.
        The REST API is what consumed by downstream applciation to consume the machine learning model that was built to complete the step to show value to business. The Rest API is realtime so the idea here is not a large volume is processed in one api rather few rows are sent to process but can be scaled for multiple clients using the container platform horizontal scaling.

    2) ReTraining process
        Once the inferencing is done now we need to make sure the model is learning as time goes by. What that means is as we collect new data after the model is deployed there should be a process to re train the model with new data and keep the model learn more and more. This is how the model keeps learning.
        Now this process is usually a batch process. It does also take a lot of time. Proper planning is needed for the retraining process as we need compute infrastruture needs.
        Since it is a batch process there is no need to run compute all the time on demand we can build the compute retrain the model save the model to docker container. Usually it monthly process that is automated. So when we create new models with retraining make sure versioning is done properly and then that version is deployed to production. Best practicses is to deploy model that improves the accuracy. There are situation where model performance might degrade and we should have proper checks not to deploy those model.
        This process can be processed using DevOps process like CI/CD or anything mechanism to autoamte the process.
        Depending on the data volume the time it takes to run this process might be few minutes to few days. Plan to scale the compute as needed to if there is a need to run faster by scaling up.

Given the above process Model building and Model Retraining process are different from what regular software application build process was.

Major changes:

1) Development needs lots of production data - large volume
    Here is where th emajor change is.
2) Development needs lots of compute to process the data for Modelling
    Here is another major change than before since in software application development usually the environment or the infrastructure is more less and sharable. Here is becomes harder with larger volume of data and time it takes to process. So don't be surprised based on use case and data scientists needs computation is going to differ. This is the reason why PaaS on demand helps a lots as and when developer need compute they can spun up and down the computation. Model building is iterative process and finding the right algorithm or neural architecture takes time by trial and error.
3) Time line for building the model can vary based on data volume.
4) Time line increases on figuring data sources and compiling data sources for use case.

Here are some reference on available platform for MLOps.
https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment