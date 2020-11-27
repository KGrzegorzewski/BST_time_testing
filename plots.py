import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def bar_PLOTSGIT(x, y, title, y_label, x_label):
  strings_x = [str(_) for _ in x]
  x = np.arange(len(x)) 
  width = 0.5  

  fig, ax = plt.subplots()
  rects = ax.bar(x, y, width)

  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_title(title)
  ax.set_xticks(x)
  ax.set_xticklabels(strings_x)
  ax.set_ylim(0, max(y) + max(y) * 0.1)
  autolabel(rects, ax)
  #plt.show()
  plt.savefig(title + ".png")
