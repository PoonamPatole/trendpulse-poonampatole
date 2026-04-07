import csv
import os

# Create data folder (important in Colab/local)
os.makedirs("data", exist_ok=True)

# Clean data (pick only required fields)
cleaned_data = []
for s in stories:
    cleaned_data.append({
        "id": s.get("id"),
        "title": s.get("title"),
        "author": s.get("by"),
        "score": s.get("score"),
        "url": s.get("url")
    })

# Save to CSV
with open("data/trends_clean.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=cleaned_data[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_data)

print("CSV file created successfully!")
