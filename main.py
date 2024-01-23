import argparse
from enum import Enum
import os
import magic
import pandas as pd
import numpy as np


class Site(str, Enum):
  # Stations
  sandton = "Sandton"
  hatfield = "Hatfield"
  rosebank = "Rosebank"
  midrand = "Midrand"

  # Parking
  sandton_park = "SandtonPark"
  hatfield_park = "HatfieldPark"
  rosebank_park = "RosebankPark"

  # Bus
  bus_point = "BusPoint"



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("csv_file", required=True)

  args = parser.parse_args()

  csv_file = args.csv_file
  if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"Travel history at {csv_file} not found")

  mimetype = magic.from_file(csv_file)
  if mimetype != "text/csv":
    raise IOError(f"File {csv_file} is not a valid CSV file")

  df = pd.read_csv(csv_file, header=1, index_col="Sequence Number", dtype={
    "Sequence Number": np.int32,
    "Transaction Date": pd.Timestamp,
    "Site": Site,
    "Transaction Type": str,
    "Remaining Trips": np.int32,
    "Transaction Value": np.float64,
    "PAYG Balance": np.float64,
  })

  print(df)
