import matplotlib.pyplot as plt
import pandas as pd
import os
df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)
