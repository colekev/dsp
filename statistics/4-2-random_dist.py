import thinkstats2
import random
import thinkplot

numbers = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(numbers)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

cdf = thinkstats2.Cdf(numbers)
thinkplot.Cdf(cdf)
thinkplot.Show()
