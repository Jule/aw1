import csv

rec = csv2rec("pipeline-bench-result.csv", delimiter=";")

grouped = defaultdict(lambda: [])

for el in rec:
    grouped[el[1]].append(el[2])

averaged = {}
for k in grouped.keys():
    averaged[k] = average(grouped[k])


x = list(averaged)
x.sort()
y = []

for k in x:
    y.append(averaged[k])





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
fig = figure()
fig.subplots_adjust(bottom=0.175, left=0.15)

plot(x,y, 'o-')
xscale("log")
ylabel('Computation time')
xlabel('Number of workers')







