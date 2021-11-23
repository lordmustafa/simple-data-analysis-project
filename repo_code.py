from functions import Data


file = 'report_data.xlsx'
f = Data(file)
#df = f.dfPrep()
#dt = f.dataPrep()
#vr = f.varPrep()
#vc = f.valCounters()
pl = f.plotting()
gr = f.grouping()

