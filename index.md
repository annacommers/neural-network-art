#Neural Network Art

The use and accessibility of machine learning and artificial intelligence has increased greatly over just the past few years. One application of this technology is 
art. AI art has been used across mediums in performances, visual pieces, music, interactive displays, and more. As AI technology continues to get more advanced, 
these projects push us to consider how we define art and how artificial intelligence will fit into our future world. For example, Stephanie Dinkins created an 
interactive talking sculpture with AI trained on oral history from a black American family (Dinkins). The piece is meant to explore the concerns and ideals of 
communities underrepresented in tech (Dinkins). Another artist, Tom White, used AI to create abstract illustrations that can be reliably classified by neural 
networks (Tom). This work allows us to see a part of how AI processes images. 

This project seeks to explore a neural network that can transform images into unique abstract art. The neural network is an autoencoder that can be trained on virtually any set of images and, after training, transform a new set of images. The code for the project uses the Tensorflow library in order to train an autoencoder on a set of images. Once trained, the autoencoder can be used to transform a new set of images into abstract art that is visually similar to the training set. The user can choose any type and number of images they want to train on. Similarly, the user can use any images they wish to transform and they can choose up to ten of them at one time.

## Results

It was found that more visually interesting results can be achieved by using visually similar training images. One type of images that worked particularly well were images of a single type of fruit. The images below were obtained by training the autoencoder on images of apples, oranges, and bananas respectively, then inputting images of artworks to be transformed.

![](websiteimages/artandapples.PNG)

![](websiteimages/bananaart.PNG)

![](websiteimages/orangeart.PNG)

link to usage instructions in README [here](https://github.com/annacommers/neural-network-art#usage)

[Download the project](https://github.com/annacommers/neural-network-art.git)

## About me
My name is Anna Commers and I am a student at Olin College of engineering. I am passionate about human centered design, software, and art. This project was made for the Software Design class at Olin College.
