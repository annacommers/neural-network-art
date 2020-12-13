import pytest
import PIL
from PIL import Image
from autoencoder import TakeInput
from autoencoder import FormatData

controller = TakeInput()
data = FormatData()

input_training_cases = [
    # Typical expected case.
    ('test', 'test', '1', None),
    # Case where file name is not valid.
    ('test', 'dsjdu', '45', True),
    # Case where folder path is not valid.
    ('akddfsauj', 'test', '45', True),
    # Case with a float.
    ('test', 'test', '1.0', True),
    # Case without a number.
    ('test', 'test', 'test', True),
]

input_testing_cases = [
    # Typical expected case.
    ('test', 'test', '1', None),
    # Case with too many images.
    ('test', 'test', '11', True),
    # Case with a float.
    ('test', 'test', '1.0', True),
    # Case where file name is not valid.
    ('test', 'dsjdu', '5', True),
    # Case where folder path is not valid.
    ('akddfsauj', 'test', '5', True),
    # Case without a number.
    ('test', 'test', 'test', True),
]


@pytest.fixture(params=input_training_cases)
def train_cases(request):
    return request.param


def test_check_train_input(train_cases):
  '''
  Test that the user input for training is checked as intended.
  '''
  train_folder, train_image, train_num, result = train_cases
  assert controller._check_train_input(train_folder, train_image, train_num) == result


@pytest.fixture(params=input_testing_cases)
def test_cases(request):
    return request.param


def test_check_test_input(test_cases):
  '''
  Test that the user input for images to transform is checked as intended.
  '''
  test_folder, test_image, test_num, result = test_cases
  assert controller._check_test_input(test_folder,
                                      test_image, test_num) == result


def test_set_file_location():
  '''
  Test that the file location can be changed correctly.
  '''
  data.set_file_location('folder1/folder2/folder3')
  assert data._file_location == 'folder1/folder2/folder3'


def test_set_image_name():
  '''
  Test that the image name can be changed correctly.
  '''
  data.set_image_name('image_name')
  assert data._image_name == 'image_name'


def test_set_image_size():
  '''
  Test that the image size can be changed correctly.
  '''
  data.set_image_size(60)
  assert data._image_size == 60


def test_get_image():
  '''
  Test that the correct image is obtained.
  '''
  data.set_file_location('test')
  data.set_image_name('test')
  image = Image.open('test/test_1.jpg')
  assert data._get_image(1) == image.convert('RGB')


def test_square_image():
  '''
  Test that image is cropped properly. 
  '''
  # Test an image that is already cropped properly.
  image = data._get_image(9).resize((data._image_size, data._image_size))
  assert data._square_image(data._get_image(9)) == image


def test_get_image_set():
  '''
  Test that the set of images is the correct dimensions (no images are
  skipped).
  '''
  matrix = data.get_image_set(10)
  assert matrix.shape == (10, data._image_size, data._image_size, 3)
