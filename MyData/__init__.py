IRAN_STOCK_DATA_PATH = "MyData/ISM"
IRAN_STOCK_INDEX_PATH = "MyData/ISM/Indicies"
CRYPTO_DATA_PATH = "MyData/crypto"
OIL_DATA_PATH = "MyData/oil"
MATALS_DATA_PATH = "MyData/metal"

from .read import read
from .download import download
from .instrument import Instrument