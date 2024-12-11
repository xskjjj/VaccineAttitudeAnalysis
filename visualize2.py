import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([['negative','pro',0.0],['negative','anti',97.62],['negative','gov',47.71],['negative','news',8.08], ['negative','other',2.17],
                    ['positive','pro',95.45],['positive','anti',0.4],['positive','gov',31.19],['positive','news',26.26], ['positive','other',2.17],
                    ['neutral','pro',4.55],['neutral','anti',1.98],['neutral','gov',21.1],['neutral','news',65.66], ['neutral','other',95.65]],
                    columns=['sentiment','column','val'])

df.pivot("column", "sentiment", "val").plot(kind='bar')

plt.ylabel("Percentage (%)")
plt.xlabel("Topics")
# plt.xticks(rotation=90)
plt.xticks(rotation=360, ha='right')
plt.title("Sentiment Engagment by Topic")
plt.show()
plt.savefig("fig1.png")
