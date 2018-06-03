# -*- coding: utf-8 -*-
##################################################################################
#WorldQuant's Exponential Smoothing Project
#date: 02/05/2018
#author: Vo Thi Quynh Yen
##################################################################################

from scipy import stats, polyfit, polyval
import numpy as np
import pandas
import matplotlib.pyplot as plt
from pylab import plot, title, show , legend, ylim, xlim
import datetime
import os

mydate = datetime.datetime.now()
month=mydate.strftime("%B")
month

# gets the current folder where this file is located
current_folder =  str(os.getcwd()+'/')

#get the sector names
dfirst = pandas.read_excel(str(current_folder+'alimentador.xlsx'))
#get time, presentes and participantes
df = pandas.read_excel(str(current_folder+'alimentador.xlsx'),skiprows=1)

#lenght of the 0th row of the excel file
lenrowzero = len(dfirst.columns)

print ' '
print' '

months = df['month counting'].values
time = np.linspace(0,len(months)-1,len(months))
print list(time)
alpha = raw_input("Enter a desired alpha number:")


def SES(series,par1):
    result = [series[0]]
    for i in xrange(0,len(series)):
        result.append(par1*series[i] + (1-par1)*result[i])

#    forecast = par1*series[len(series)-1] + (1-par1)*result[len(series)-1]
#    result.append(forecast)
    return result


SES_presentes = []
SES_participantes = []
setores = []
for i in xrange(0,lenrowzero,4):
    setores.append(dfirst.columns[i])


#for i in xrange(0,len(setores)):
#    print setores[i]



f = open(str('forecasts_adesao_'+str(month)+'.txt'),'w')
g = open(str('forecasts_demand_'+str(month)+'.txt'),'w')

for i in xrange(0,len(setores)):
    if i == 0:
       value_pre = str('Presentes')
       value_par = str('Participantes')
    else:
       value_pre = str('Presentes'+'.'+str(i))
       value_par = str('Participantes'+'.'+str(i))


    presentes = df[value_pre].values
#    print 'maximo', max(presentes)
    participantes = df[value_par].values


# here we call the function that performs the forecast
    SES_presentes.append(SES(presentes,alpha))
    forecast_presentes = SES(presentes,alpha)[len(SES_presentes[i])-1]
    SES_participantes.append(SES(participantes,alpha))
    forecast_participantes = SES(participantes,alpha)[len(SES_participantes[i])-1]
    forecast_adesao = str(100.0*forecast_participantes/forecast_presentes)


    print ' '
    print setores[i]
    print 'presentes: ', presentes
    print 'complete forecast series (presentes): ',SES_presentes[i]
    print 'forecast presentes: ',forecast_presentes
    print 'participantes: ', participantes
    print 'complete forecast series (participantes): ',SES_participantes[i]
    print 'forecast participantes: ',forecast_participantes
    print 'forecast adesao (%): ',forecast_adesao
    print ' '


    timep1 = list(time)
    timep1.append(len(presentes))

    figurename = str(setores[i].replace(" ","")+'_forecast'+'_'+str(month)+'.png')

    plt.figure(i+1)
    plt.title(str('SES forecasting:'+' '+setores[i]))
    plt.plot(time,presentes,'g.--')
    plt.plot(timep1,SES_presentes[i],'b.-')
    plt.plot(time,participantes,'r.--')
    plt.plot(timep1,SES_participantes[i],'k.-')
    plt.ylim([0,1.10*max(presentes)])
    plt.xlim([0,len(time)+2])
    plt.legend(['time series (presentes)', 'SES forecast (presentes)', 'time series (participantes)',
                'SES forecast (participantes)' ], loc='upper left',fontsize = 'x-small')
    plt.savefig(figurename, bbox_inches='tight')







    f.write("%s\n\n" % str(setores[i]+',  '+forecast_adesao+'%'))
    g.write("%s\n\n" % str(setores[i]+',  '+str(int(forecast_participantes))))


f.close()
g.close()