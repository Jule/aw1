def progress_plot():
    start_year = 2005
    end_year = 2007
    #x = linspace(start_year, end_year, (end_year - start_year)+1)


    acm_concurrency = {
        "2005": 846,  # 20314 -> .041646155
        "2006": 953,  # 21635 -> .044048995
        "2007": 1148, # 22383 -> .051288925
        "2008": 1110, # 22392 -> .049571275
        "2009": 1173, # 26355 -> .044507684
        "2010": 1273, # 28323 -> .044945804
        "2011": 1356, # 28737 -> .047186554
        "2012": 1442, # 30614 -> .047102633
    }

    ieee_concurrency = {
        "2005": 235,
        "2006": 248,
        "2007": 281,
        "2008": 288,
        "2009": 320,
        "2010": 358,
        "2011": 316,
        "2012": 338,
    }

    acm_total = {
        "2005": 20314.0,
        "2006": 21635.0,
        "2007": 22383.0,
        "2008": 22392.0,
        "2009": 26355.0,
        "2010": 28323.0,
        "2011": 28737.0,
        "2012": 30614.0,
    }

    x = acm_total.keys()
    x.sort()
    #x = x[1:] # Take out the first year

    y = []
    for year in x:
        curr = acm_concurrency[year]
        #prev = acm_concurrency[str(int(year)-1)]
        y.append(curr)

    y1 = []
    for year in x:
        curr = ieee_concurrency[year]
        #prev = ieee_concurrency[str(int(year)-1)]
        y1.append(curr)
        #y1.append(ieee_concurrency[year])



    # plert
    plot(x,  y, 'o-', x, y1, 'o-')

    # x-axis ticks should appear as 2007, 2008, etc, not 2.0 + 2.005*10^3
    locs,labels = xticks()
    xticks(locs, map(lambda x: "%g" % x, locs))


    leg = legend(tuple(["ACM Digital Library", "IEEE Explore"]), "upper left", fancybox=True)
    leg.get_frame().set_alpha(0.5)



#http://wiki.scipy.org/Cookbook/Matplotlib/LaTeX_Examples
def eps_plot(target):
    fig_width_pt = 217.62206
    inches_per_pt = 1.0/72.27
    golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height = fig_width*golden_mean      # height in inches
    fig_size =  [fig_width,fig_height]

    params = {'backend': 'ps',
                 'axes.labelsize': 10,
                 'text.fontsize': 10,
                 'legend.fontsize': 10,
                 'xtick.labelsize': 8,
                 'ytick.labelsize': 8,
                 'text.usetex': False,
                 'figure.figsize': fig_size}
    rcParams.update(params)
    fig = figure()
    #fig.subplots_adjust(bottom=0.15, left=0.15)

    progress_plot()
    ylabel('Publications with keyword "concurrency"')
    xlabel('Year')

    savefig(target)


