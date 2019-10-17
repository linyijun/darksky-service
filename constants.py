from data_models.data_model import *
from data_models.grid_model import *


LOS_ANGELES = {
    "TARGET_LOC": LosAngeles5000mGrid,
    "DARKSKY_OBJ": LosAngeles5000mGridMeoDarkSky201801,
    "API_KEY": 'fb6117940de78d7928081f9680c93aac',
    "MAX_RETRY": 5
    }


UTAH = {
    "TARGET_LOC": SalkLakeCity5000mGrid,
    "DARKSKY_OBJ": SaltLakeCity5000mGridMeoDarkSky201703201803,
    "API_KEY": 'fb6117940de78d7928081f9680c93aac',
    "MAX_RETRY": 5
    }
