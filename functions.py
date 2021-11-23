import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Data:
    def __init__(self, data):
        self.data = data
        self.attrDic = {}
        self.Li = [
                    'STATES',
                    'GENDER',
                    'GREEN SPACES',
                    'UNIVERSITY SHAPE',
                    'SERVICES',
                    'CAFE EXISTENCE',
                    'SERVICES EFFECT',
                    'UNIVERSITY TYPE',
                    'EXPENSES',
                    'EXPENSES EFFECT',
                    'DISTINATION BETWEEN HOUSE UNIVERSITY',
                    'UNIVERSITY PLACE EFFECT',
                    'E-LEARNING EXPERMENT',
                    'E-LEARNING ENVIRONMENT',
                    'E-LEARNING EFFECT',
                    'C-LEARNING EXPEREMENT',
                    'UNIVERSITY SATISFICATION'
                    ]
        
        self.colors = ['#1f77b4', 
                       '#ff7f0e', 
                       '#2ca02c', 
                       '#d62728', 
                       '#9467bd', 
                       '#8c564b', 
                       '#e377c2', 
                       '#7f7f7f', 
                       '#bcbd22', 
                       '#17becf',
                       '#876587',
                       '#fab324']

    
    def dfPrep(self):
        f = pd.read_excel(self.data)
        df = pd.DataFrame(f)
        return df
    
    def dataPrep(self):
        self.dfPrep().dropna()
        attrArr = np.array(self.dfPrep().columns)
        for i in range(len(attrArr)):
            if 'Unnamed' in attrArr[i] or attrArr[i] in ['names', 'uni', 'college_stage']:
                np.delete(attrArr, i)
                self.dfPrep().drop(self.dfPrep().columns[i], axis=1, inplace=True)
            else:
                self.attrDic.update({attrArr[i] : list(self.dfPrep()[attrArr[i]].drop_duplicates())})
        return attrArr      
    
    def valCounters(self):
        countDic = {}
        for i in self.dataPrep():
             if 'Unnamed' in i or i in ['names', 'uni', 'college_stage']:
                list(self.dfPrep()).remove(i)
                self.dfPrep().drop(i, axis=1, inplace=True)
             else:
                countDic.update({i:dict(self.dfPrep()[i].value_counts())})
                countDf = pd.DataFrame(countDic)
        return countDf
    
    def indexPrep(self):
        indexLi = list(self.valCounters().index)
        return indexLi
    
    def plotting(self):
        c = 0
        for i in self.dataPrep():
            if 'Unnamed' in i or i in ['names', 'uni', 'college_stage']:
                list(self.dfPrep()).remove(i)
                self.dfPrep().drop(i, axis=1, inplace=True)
            else:
                pl = self.dfPrep()[i].value_counts()
                pl.plot(kind ='bar',
                    figsize=(12, 10),
                    color=self.colors,
                    fontsize=(18))
                plt.style.use('ggplot')
                plt.title(self.Li[c])
                c += 1
                plt.show()
                
                
    def grouping(self):
        c = 2
        attrLi = [i for i in self.dataPrep() if i not in ['Unnamed: 0', 'names', 'uni', 'college_stage', 's_type', 'states']]
        for i in attrLi:
            stgDf = self.dfPrep()['states'].groupby(self.dfPrep()[i]).value_counts()
            sgDf = self.dfPrep()['s_type'].groupby(self.dfPrep()[i]).value_counts()
            plt.bar
            plt.style.use('bmh')
            stgDf.plot(kind ='bar',
                figsize=(12, 10),
                color=self.colors,
                title=f'STATES WITH {self.Li[c]}',
                fontsize=(18))
            plt.show()
            
            sgDf.plot(kind ='bar',
                figsize=(12, 10),
                color=self.colors,
                title=f'GENDER WITH {self.Li[c]}',
                fontsize=(18))
            plt.show()
            c += 1