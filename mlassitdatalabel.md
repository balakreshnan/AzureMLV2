# ML Assited Data labelling 

## Use Case

To Apply Machine learning or Deep Learning on any image or vision based project first images has to be tagged.
Tagging image is labor intensive work and take long time. How can we make it much more productive is what we are going to see.

To solve the above we are going to use the Azure Machine learning service - Data Labelling features which has Manual and ML Assited tagging. 

What is ML Assisted Tagging?

Lets take like 2000 pictures and take two tags or 1000 images with one tag for example like face mask. For the below tutorial i am using only few images but for ML assit to work we need more images. Once you collected the image then tag around 100 of them for 1000 images manual. Options availble to have multiple people can tag the images.

Once the images are tag then wait until the ML assit does it job. For ML assit we need GPU based cluster and also make sure select a region where GPU based virtual machines are available.

Steps to do

- Collect images
- Create a Blob Storage
- Create a container 
- Upload the images
- Create a Azure Machine learning Services - i choose WEST US 2 since GPU was available
- Create a Data Labeling project
- Create Data Set from Data Store
- Create project
- Image Tagging
- ML Assit tagging

Collect images 
Create a Blob Storage 
Create a container 
Upload the images 

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask1.jpg "Face mask")

Create a Azure Machine learning Services - i choose WEST US 2 since GPU was available 
Create a Data Labeling project 

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask1.jpg "Face mask")

Create Data Set from Data Store

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask2.jpg "Face mask")
![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask3.jpg "Face mask")
![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask4.jpg "Face mask")

Add Class or Label

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask5.jpg "Face mask")

Labelling Instruction

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask6.jpg "Face mask")

Create project

Select ML Assit

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask7.jpg "Face mask")

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask8.jpg "Face mask")

Image Tagging

Select the project

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask9.jpg "Face mask")

Click Data Label

Start Labeling

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask10.jpg "Face mask")

ML Assit tagging

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask11.jpg "Face mask")

Tag all the images until the UI says it says there is no tasks

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask12.jpg "Face mask")

Go back to Project Screen

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask13.jpg "Face mask")

Click Details

![alt text](https://github.com/balakreshnan/AzureMLV2/blob/master/images/facemask14.jpg "Face mask")

Wait until remaining is all completed. 

In our say if you had 1000 images you need to tag 100 and then it takes time to do ML assisted tagging.