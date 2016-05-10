import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in('goutham.muppala', 'pvajpur7ig')

data1 = np.genfromtxt('3clients/u1.csv', delimiter=',', skip_header=1,
                     skip_footer=0, names=['EpochTime','CurrentPlaybackTime','CurrentBufferSize','CurrentPlaybackState','Action','Bitrate']);

data2 = np.genfromtxt('3clients/u2.csv', delimiter=',', skip_header=1,
                     skip_footer=0, names=['EpochTime','CurrentPlaybackTime','CurrentBufferSize','CurrentPlaybackState','Action','Bitrate']);

data3 = np.genfromtxt('3clients/u1.csv', delimiter=',', skip_header=1,
                     skip_footer=0, names=['EpochTime','CurrentPlaybackTime','CurrentBufferSize','CurrentPlaybackState','Action','Bitrate']);


trace1 = go.Scatter(
    x = data1['EpochTime'],
    y = data1['Bitrate'],
    mode = 'lines',
    name = 'lines'
)

trace2 = go.Scatter(
    x = data2['EpochTime'],
    y = data2['Bitrate'],
    mode = 'lines',
    name = 'lines'
)

trace3 = go.Scatter(
    x = data3['EpochTime'],
    y = data3['Bitrate'],
    mode = 'markers',
    name = 'markers'
)

data=[trace1,trace2,trace3]

py.iplot(data, filename='line-mode')
