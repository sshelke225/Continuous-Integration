import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [10, 50, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:green']

ax.bar(fruits,counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.savefig('bar.png', bbox_inches='tight')

cat = ["bored", "happy", "happy", "happy", "happy", "bored"]
dog = ["happy", "happy", "bored", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig,ax = plt.subplots()
ax.plot(activity,dog,label='dog')
ax.plot(activity,cat, label=cat)
ax.legend()

plt.savefig('lines.png',bbox_inches='tight')