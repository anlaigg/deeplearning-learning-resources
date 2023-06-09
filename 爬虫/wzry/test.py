import os
from matplotlib import pyplot as plt
#新增加的两行
import matplotlib
matplotlib.rc("font",family='YouYuan')

hero_stats = {'英雄名字': '云缨', '生存能力': '10', '攻击伤害': '7', '技能效果': '8', '上手难度': '8'}


# Extract the keys and values from the dictionary
stats_labels = list(hero_stats.keys())[1:]
stats_values = [int(val) for val in list(hero_stats.values())[1:]]

# Create a bar chart using Matplotlib
plt.bar(stats_labels, stats_values)

# Add labels and a title to the chart
plt.xlabel('Stat')
plt.ylabel('Value')
plt.title('Hero Stats for ' + hero_stats['英雄名字'])

# Create the "img" folder if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# Display the chart
plt.savefig(f"img/{hero_stats['英雄名字']}.png")
plt.show()

