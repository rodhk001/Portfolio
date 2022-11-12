# Breast Ultrasound Image Classification
## By Kiana Gonzalez-Rodholm
### Project Summary
This project uses image classification on normal, benign, and malignant breast ultrasound images to build a model that can detect whether a specific specimen contains cancer or not. The business problem would be that there needs to be a way to detect whether a person has breast cancer quickly and in an automated way to test for cancer based off someone’s ultrasound images. This could therefore speed up the process of diagnosing patients and getting them the treatment they need. Some research questions to answer include the following: With what accuracy and speed can we determine if an ultrasound image contains cancerous masses. What would be the impact if an image is misclassified? What is it that determines whether an image has cancerous masses? 

### Methods
Some of the methods used for this analysis included a model using a 2D convolution layer, as well as max pooling, flattening, and dense layers. An Adam optimizer and sparse categorical cross entropy to measure loss was used for compiling the model. Using matplotlib I created line/scatter plots of the training and validation loss and accuracy. I then was able to pull the result of the predictions into a confusion matrix and then create heatmap of the results using the seaborn package. Pandas, NumPy, OS, Pathlib, and OpenCV modules were also used to upload and manipulate the data into the proper format for modeling.

### Results and Future Application
Throughout various manimpulation of the model and the parameters, I was able to get a model with %76 percent accuracy on the test data. With the small amount of data given, I believe a fairly accurate and reliable model was created. With the use of machine learning and data cleaning and visualization, this model can be used to further aid in medical research and testing on patients. Since women get mammograms routinely, this model can help to expedite the testing process in order to get women (or men) the treatment they need.

**Note:** This data was too large to fit on this repository, but can be found and downloaded here: [Ultrasound Images](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset)
