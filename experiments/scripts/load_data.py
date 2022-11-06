from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import tensorflow as tf
from tensorflow.keras.layers import Rescaling
from scripts.constants import get_constants

def load_dataset(name, normalize=False, batch=False, colab=False):
    constants = get_constants()
    seed = constants['random_seed']
    constants = constants[name]

    dataset = tf.keras.utils.image_dataset_from_directory(
        directory=constants['colab'] if colab else constants['local'], 
        labels=None, 
        color_mode=constants['color_mode'], 
        image_size=(constants['height'], constants['width']), 
        batch_size=None,
        shuffle=True, 
        seed=seed, 
        validation_split=None, 
        subset=None, 
        interpolation='bilinear', 
        follow_links=False
    )

    if normalize:
        normalization_layer = Rescaling(constants['normalization_factor'])
        dataset = dataset.map(lambda x: normalization_layer(x))

    if batch:
        dataset = dataset.batch(constants['batch_size'])


    return dataset