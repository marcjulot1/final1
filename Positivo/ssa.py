import pandas as pd
import random
from api import result
df = pd.DataFrame(list(result))
pd.set_option('display.max_colwidth', 1)
list = df.tail(-1)
print(list)
