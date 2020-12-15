# Neural Network Art

This project allows users to train an autoencoder neural network on virtually any set of images, then use the trained autoencoder to transform a new set of between one and ten images into pieces of art. 

## Usage

It is recommended that the code provided in `neural-network-art.ipynb` be used in a google colab notebook. The autoencoder relies on the Tensorflow library which is well suited to work in the colab environment. To use the program as is, run the code cell in the notebook `neural-network-art.ipynb`. This will run the `main` function which puts all of the classes together. More information on each class is below. In order to train the autoencoder, the `TakeInput` class asks the user for the path to the training images, the name of the training images, and the number of training images. Similarly, to add new images to transform, it asks for a folder path, the name of the images, and the number of images (up to ten). More information on data is below. 

## Classes

### Autoencoder

The `Autoencoder` class relies on the Tensorflow library in order to train an autoencoder neural network on a numpy array representing a set of training images, then transform a second numpy array of testing images. The autoencoder consists of an input layer, an output layer, and a 64 dimention latent vector between them. If you wish to change the dimension of this latent vector, call the `set_latent_dimension` method with the number of dimensions desired. Additionally, the number of epochs can be changed with the `set_epochs()` method. 

### TakeInput

The `TakeInput` class prompts the user to input the folder location for training and testing images, the name of training and testing images, and the number of training and testing images. It checks this input to ensure there are files in the locations provided and the number values are valid.

### ViewImages

The `ViewImages` class takes the testing images and displays them before and after going through the autoencoder.

### FormatData

The `FormatData` class takes file locations for image files and formats the images into a numpy array for use in the `Autoencoder` class. The `set_file_location` method can be used to determine the path for the folder with your images. The `set_image_name` method determines the name of the images. The `set_image_dimention` method sets the pixel dimention (used when cropping the image into a square). Lastly, the `get_image_set` method returns a numpy array of images based on the file location set and the number of images desired. 

## Data

Both training and testing data must follow the naming sceme 'name_1.jpg', 'name_2.jpg', etc. Virtually any type and number of images can be used to train as long as they can be found in a single folder with proper naming. There can be gaps in your training images such as having 'name_1.jpg' and 'name_3.jpg' but not 'name_2.jpg'. If this is the case, input that you want to train on 3 images and the second image will be skipped if not found. While there can be gaps in the training images, there must be an image called 'name_1.jpg'. Testing images follow the same naming system, but can not have gaps between them. You can have between 1 and 10 of them, and if you input that you want to transform 10 there must be images 'name_1.jpg', 'name_2.jpg',...,'name_10.jpg' in the folder specified. 

Sample training and testing images may be downloaded from this repository. The `train` folder includes images of fruit (apples, bananas, and oranges). The `test` folder includes ten images of artworks. While any images can be used for testing and training, often best results are achieved with training images that are visually similar (such as images of a single type of fruit). 

## Testing

The files `autoencoder.py` and `test_autoencoder.py` are included in this repository for testing purposes. Testing also relies on having the folder `test` with sample images.

## Authors and Acknowlegment 

This project was written by Anna Commers with guidance from Steve Matsumoto, for the software design class at Olin College of Engineering.
