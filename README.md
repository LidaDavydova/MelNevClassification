# MelNevClassification

## RU version
MelNevClassification - проект, нацеленный на решение проблемы распознавания (классифицирования) раковых новообразований на теле, в частности, меланом и родинок. Мы выделили именно эти 2 категории,






## EN version

The purpose of work is to research different implementatons of **melanoma/nevus** recognition and classification on the picture.
Moreover, in the end we should have trained model on our dataset.

Dataset was created by open source skin cancer datasets:

![HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

ISIC Challenge sourses:

![ISIC Challenge 2024](https://challenge2024.isic-archive.com/)

![ISIC Challenge 2020](https://challenge.isic-archive.com/data/#2020)

![ISIC Challenge 2019](https://challenge.isic-archive.com/data/#2019)

## Data processing
![data_distrib](https://github.com/user-attachments/assets/5cee4c3f-36e6-4f7c-b714-842d53754baa)




## About model

## Image classification model

model-72.keras in MelNev_train.ipynb has accuracy on test images ~ 0.72

**kerasSimple.h5** in folder _models/_

It consist of 3 layers of convolution
![architecture](https://github.com/user-attachments/assets/0962f7e0-67e4-4fcb-99f0-eb2131bc134c)


### Statistic of training and validation for model:
![Screenshot from 2024-02-13 19-28-26](https://github.com/LidaDavydova/MelanomaVenusClassification/assets/79317010/0aa3660f-adec-4b01-9412-bec9179bba24)

The second model model_keras_2_1.keras in dataset.ipynb has accuracy on test images ~ 0.82

**model_keras_2_1.keras** in folder _models/_

It consist of 3 layers of convolution

### Statistic of training and validation for model:
![Screenshot from 2024-08-17 20-52-02](https://github.com/user-attachments/assets/c5c58433-b7a0-4287-b016-9061e2207aad)


## Parameterized data from images classification models

The model model_sklearn_1_0.pkl has accuracy on test images ~ 0.87

It depends of quality of the **image classification model**

**model_sklearn_1_0.pkl** in folder _models/_

### Statistic of trained model:
![Screenshot from 2024-08-17 21-20-51](https://github.com/user-attachments/assets/2d36204b-520d-4182-a896-232db1369804)

## Try it

In file testModel.ipynb you can check model on your images

### Web site:
http://89.169.135.79:5000/

## Telegram Bot:
https://t.me/AntiMelonomabot
