from models.data_model import LosAngeles5000mGridMeoDarkSky2018
from models.grid_model import LosAngeles5000mGrid


LOS_ANGELES = {
    "TARGET_LOC": LosAngeles5000mGrid,
    "DARKSKY_TABLE": LosAngeles5000mGridMeoDarkSky2018,
    "API_KEY": '',
    "MAX_RETRY": 5
    }
