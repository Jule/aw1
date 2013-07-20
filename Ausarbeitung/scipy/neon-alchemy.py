data = (
    ("NEON with Preload", 11.946),
    ("NEON", 4.929),
    ("ARM Assembly", 2.63),
    ("C", 1)
)



# xlabel("FOO")
# ylabel("FOO")
# title("Testing")

# x = range(len(data))
# y = [d[1] for d in data]

# # def millions(x, pos):
# #     'The two args are the value and tick position'
# #     return '$%1.1fM' % (x*1e-6)

# #formatter = FuncFormatter(millions)

# #ax = subplot(111)
# #ax.yaxis.set_major_formatter(formatter)
# bar(x, y)
# locs,labels = xticks()
# #xticks( locs,  ('Bill', 'Fred', 'Mary', 'Sue') )
# xticks(x, map(lambda xx: data[xx][0], x))
# show()

#val = 3+10*rand(5)    # the bar lengths
pos = arange(len(data))+.5    # the bar centers on the y axis

x = range(len(data))
y = [d[1] for d in data]
labels = tuple([d[0] for d in data])




fig_width_pt = 217.62206
inches_per_pt = 1.0/72.27
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]

print fig_size

params = {'backend': 'ps',
             'axes.labelsize': 5,
             'text.fontsize': 5,
             'legend.fontsize': 5,
             'xtick.labelsize': 5,
             'ytick.labelsize': 5,
             'text.usetex': False,
             'figure.figsize': fig_size}
rcParams.update(params)
fig = figure(1)
fig.subplots_adjust(bottom=0.175, left=0.24)



barh(pos, y, align='center', facecolor='#c0c0c0')
yticks(pos, labels)
xlabel('Performance')
#title('How fast do you want to go today?')
grid(True)

savefig("test.pdf")
