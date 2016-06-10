
import thinkstats2
import chap01soln
import thinkplot

resp = chap01soln.ReadFemResp()

numkdhh_hist = thinkstats2.Hist(resp.numkdhh)

thinkplot.Hist(numkdhh_hist)
thinkplot.show(xlabel='# children', ylabel ='frequency')

numkdhh_pmf = thinkstats2.Pmf(resp.numkdhh)

thinkplot.Pmf(numkdhh_pmf)
thinkplot.show(xlabel='# children', ylabel ='probability')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

numkdhh_biased = BiasPmf(numkdhh_pmf, label='biased')

thinkplot.Pmf(numkdhh_biased)
thinkplot.Show(xlabel='# children', ylabel ='probability')

thinkplot.PrePlot(2)
thinkplot.Pmfs([numkdhh_pmf, numkdhh_biased])
thinkplot.Show()

numkdhh_pmf.Mean()

numkdhh_biased.Mean()
