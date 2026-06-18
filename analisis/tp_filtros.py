import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Indian_Student_AI_Dataset.csv")

print(df.columns)