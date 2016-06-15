import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

low = (5*12+10)*2.54
high = (6*12+1)*2.54

low_cdf = dist.cdf(low)
high_cdf = dist.cdf(high)
diff = high_cdf - low_cdf
print(diff)
