import statistics
import random
import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
data1 = pd.read_csv('medium_data.csv')
listdata=data1['reading_time'].tolist()
mean=statistics.mean(listdata)
print('Pm=',mean)
stddev=statistics.stdev(listdata)
print('Psd=',stddev)    
def randSample(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(listdata)-1)
        value=listdata[randomindex]
        dataset.append(value)
    mean2=statistics.mean(dataset)
    return(mean2)
meanlist=[]
for i in range(0,30):
    setofmeans=randSample(100)
    meanlist.append(setofmeans)
mean3=statistics.mean(meanlist)
stdev2=statistics.stdev(meanlist)
print('Mean of the sample= ',mean3)
print('Standard deviation= ',stdev2)
deviation=statistics.stdev(listdata)
firstStandardDeviationStart,firstStandardDeviationEnd=mean3-deviation,mean3+deviation
secondStandardDeviationStart,secondStandardDeviationEnd=mean3-(2*deviation),mean3+(2*deviation)
thirdStandardDeviationStart,thirdStandardDeviationEnd=mean3-(3*deviation),mean3+(3*deviation)
print(deviation)
figure=ff.create_distplot([meanlist],['reading_time'],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode='lines'))
figure.add_trace(go.Scatter(x=[firstStandardDeviationStart,firstStandardDeviationStart],y=[0,0.17],mode='lines',name='First Standard Deviation'))
figure.add_trace(go.Scatter(x=[firstStandardDeviationEnd,firstStandardDeviationEnd],y=[0,0.17],mode='lines',name='First Standard Deviation')) 
figure.add_trace(go.Scatter(x=[secondStandardDeviationStart,secondStandardDeviationStart],y=[0,0.17],mode='lines',name='Second Standard Deviation')) 
figure.add_trace(go.Scatter(x=[secondStandardDeviationEnd,secondStandardDeviationEnd],y=[0,0.17],mode='lines',name='Second Standard Deviation')) 
figure.add_trace(go.Scatter(x=[thirdStandardDeviationStart,thirdStandardDeviationStart],y=[0,0.17],mode='lines',name='Third Standard Deviation')) 
figure.add_trace(go.Scatter(x=[thirdStandardDeviationEnd,thirdStandardDeviationEnd],y=[0,0.17],mode='lines',name='Third Standard Deviation')) 
figure.show()