from pathlib import Path
import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt

Path("img").mkdir(exist_ok=True)

plt.figure(figsize=(12, 4))
plt.axis("off")
plt.text(0.01, 0.65, "What Influences Developer Salaries?", fontsize=26, weight="bold")
plt.text(0.01, 0.30, "Insights from the Stack Overflow Developer Survey", fontsize=16)
plt.text(0.01, 0.05, "Work experience • Job satisfaction • Baseline salary model", fontsize=12)
plt.tight_layout()

plt.savefig("img/blog_thumbnail.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved: img/blog_thumbnail.png")