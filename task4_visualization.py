import matplotlib.pyplot as plt
import pandas as pd
import os
df = pd.read_csv("data/trends_anaylised.csv")
os.makedirs("outputs", exist_ok=True)

Score=np.array(['A','B','C','D','E'])
score_arr=np.array([466,88,44,26,292])
plt.bar(Score,score_arr)
plt.savefig("chart1_top_stories.png")
print("The Figure Path is=",os.getcwd())
plt.show()

# Count categories
types = [story.get('type', 'unknown') for story in stories if story]
category_counts = Counter(types)

categories = list(category_counts.keys())
counts = list(category_counts.values())

print(categories, counts)  # debug

# Create new figure
plt.figure(figsize=(6,4))

# Plot
plt.bar(categories, counts)

plt.title("Number of Stories by Category")
plt.xlabel("Category (Type)")
plt.ylabel("Number of Stories")
plt.tight_layout()
plt.savefig("chart2_categories.png")
plt.show()
# “The dataset contains only one category (‘story’), so the bar chart displays a single bar."
