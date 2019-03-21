import numpy as np

# NAME:
#         avrg
# PURPOSE:
#         Average 1d-array data in a interval of N points
# CALLING SECUENCE:
#         data_avrg = avrg_data(data,N)
# OUTPUTS:
#         data_avrg (Average data in N points)
# MODIFICATION HISTORY:
#         Created by Ray Hidalgo 2015-03-30
def avrg_data(data,N):
    N = float(N)
    return np.array([np.nanmean(i) for i in np.array_split(data,len(data)/N)])

# NAME:
#         std_data
# PURPOSE:
#         Standard deviation 1d-array data in a interval of N points
# CALLING SECUENCE:
#         std_data = data_std(data,N)
# OUTPUTS:
#         data_avrg (Average data in N points)
# MODIFICATION HISTORY:
#         Created by Ray Hidalgo 2017-11-23
def std_data(data,N):
    N = float(N)
    return np.array([np.nanstd(i) for i in np.array_split(data,len(data)/N)])
