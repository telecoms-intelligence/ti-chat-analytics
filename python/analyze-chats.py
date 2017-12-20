#!/usr/bin/env python3

import pandas as pd
import numpy as np
import bz2
import json

#
with bz2.BZ2File("data/sms/smsCorpus_en_2015.03.09_all.json.bz2") as json_file:
  data = json.load(json_file)

df = pd.DataFrame(data)
print (str(df))

