
# <p align="center" width="100%">MelNevClassification</p>
### RU версия 
## Описание
MelNevClassification - проект, нацеленный на решение проблемы распознавания (классифицирования) раковых новообразований на теле, в частности, меланом и родинок с помощью анализа дермотологическихснимков сверточной нейронной сетью. Мы выделили именно эти 2 класса (меланома и родинка), чтобы посмотреть на динамику обучения нейронной сети.

Дермотологические снимки для обучения и тестирования были взяты из официальных открытых источников.

## Протестируйте сами тут

### Telegram Bot: https://t.me/MelNev_bot

Или запуском программы для тестирования - запустить файл testModel.ipynb


## Источники данных
![HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

ISIC Challenge:

![ISIC Challenge 2024](https://challenge2024.isic-archive.com/)

![ISIC Challenge 2020](https://challenge.isic-archive.com/data/#2020)

![ISIC Challenge 2019](https://challenge.isic-archive.com/data/#2019)

## Детали реализации
### Обработка данных
Из выбранных источников, описанных выше, были взяты только снимки меланом и родинок. Вышло следующее:
![classes](https://github.com/user-attachments/assets/2d46d462-b250-4c8f-9cac-00c14cdef819)

Чтобы увеличить количество изображений меланом, мы попробовали убрать волосы на изображениях кожи, где они были, тем самым увеличили датасет на 800 фоток.

Пример: 

![hair_remove_example](https://github.com/user-attachments/assets/488fee69-4af9-44c5-9f59-c0df29ea6f8f)

Затем появилась идея попробовать менять цвет кожи, создавая свои маски для некоторых снимков.

Пример:

![mask_example1](https://github.com/user-attachments/assets/aa791be4-1401-49c8-928b-151f6515d08a)
![mask_example2](https://github.com/user-attachments/assets/f496463f-822b-4074-b438-e705033b1d2a)


Для обучения классы изображений должны быть +- одинакого распределены, поэтому мы собрали датасет из следующего количества:

![data_distrib](https://github.com/user-attachments/assets/221553c3-a0a5-4597-a0eb-0d8df138c6a7)


### Обучение нейронной сети
В файле *MelNev_train.ipynb* показано обучение модели **model-72.keras**.

Ее архитектура:

<img src="https://github.com/user-attachments/assets/84e0f75d-8206-4460-908f-0a121f396565" width="50%" />

История обучения:

<img src="https://github.com/user-attachments/assets/4c6eb505-50f2-4696-a4ca-7864042b3fbe" width="50%" />

Показания тестирования обученной нейронной сети:

**72% точность**

<img src="https://github.com/user-attachments/assets/d9a77322-eea4-411b-a74c-92a95ca04d52"/>


## EN version
## Description
MelNevClassification is a project aimed at solving the problem of recognizing (classifying) cancerous neoplasms on the body, in particular melanomas and moles, using a convolutional neural network to analyze dermatological images. We identified these two classes (melanoma and mole) to look at the dynamics of neural network training.

Dermatological images for training and testing were taken from official open sources.

## Test it yourself here

### Telegram Bot: https://t.me/MelNev_bot

Or by running the testing program - run the testModel.ipynb file

## Data sources
![HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

ISIC Challenge:

![ISIC Challenge 2024](https://challenge2024.isic-archive.com/)

![ISIC Challenge 2020](https://challenge.isic-archive.com/data/#2020)

![ISIC Challenge 2019](https://challenge.isic-archive.com/data/#2019)

## Implementation details
### Data processing
From the selected sources described above, only images of melanomas and moles were taken. The following came out:
![classes](https://github.com/user-attachments/assets/2d46d462-b250-4c8f-9cac-00c14cdef819)

To increase the number of melanoma images, we tried to remove hair from skin images where it was, thereby increasing the dataset by 800 photos.

Example:

![hair_remove_example](https://github.com/user-attachments/assets/488fee69-4af9-44c5-9f59-c0df29ea6f8f)

Then an idea came up to try changing the skin color by creating our own masks for some images.

Example:

![mask_example1](https://github.com/user-attachments/assets/aa791be4-1401-49c8-928b-151f6515d08a)
![mask_example2](https://github.com/user-attachments/assets/f496463f-822b-4074-b438-e705033b1d2a)

For training, the image classes should be +- equally distributed, so we collected a dataset from the following amount:

![data_distrib](https://github.com/user-attachments/assets/221553c3-a0a5-4597-a0eb-0d8df138c6a7)

## Implementation details
### Data processing
From the selected sources described above, only images of melanomas and moles were taken. The following came out:
![classes](https://github.com/user-attachments/assets/2d46d462-b250-4c8f-9cac-00c14cdef819)

To increase the number of melanoma images, we tried to remove hair from skin images where it was, thereby increasing the dataset by 800 photos.

Example:

![hair_remove_example](https://github.com/user-attachments/assets/488fee69-4af9-44c5-9f59-c0df29ea6f8f)

Then an idea came up to try changing the skin color by creating our own masks for some images.

Example:

![mask_example1](https://github.com/user-attachments/assets/aa791be4-1401-49c8-928b-151f6515d08a)
![mask_example2](https://github.com/user-attachments/assets/f496463f-822b-4074-b438-e705033b1d2a)

For training, the image classes should be +- equally distributed, so we collected a dataset from the following amount:

![data_distrib](https://github.com/user-attachments/assets/221553c3-a0a5-4597-a0eb-0d8df138c6a7)
