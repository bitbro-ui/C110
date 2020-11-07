import pandas as pd 
import statistics
import csv
import plotly.figure_factory as ff

reader = pd.read_csv('C:/Users/arkma/Dropbox/My PC (DESKTOP-F2428EU)/Downloads/data1.csv')
hlist = reader["Height(Inches)"].to_list()
wlist = reader["Weight(Pounds)"].to_list()

hmean = statistics.mean(hlist)
wmean = statistics.mean(wlist)

hmedian = statistics.median(hlist)
wmedian = statistics.median(wlist)

hmode = statistics.mode(hlist)
wmode = statistics.mode(wlist)

print("mean median mode of height is {},{},{}".format(hmean,hmedian,hmode))
print("mean median mode of weight is {},{},{}".format(wmean,wmedian,wmode))

height_std_deviation = statistics.stdev(hlist)
weight_std_deviation = statistics.stdev(wlist)

print("standard deviation of height is {}".format(height_std_deviation))
print("standard deviation of weight is {}".format(weight_std_deviation))

height_first_std_deviation_start, height_first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation 
height_second_std_deviation_start, height_second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_third_std_deviation_start, height_third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation) 
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in hlist if result > height_first_std_deviation_start and result < height_first_std_deviation_end] 
height_list_of_data_within_2_std_deviation = [result for result in hlist if result > height_second_std_deviation_start and result < height_second_std_deviation_end] 
height_list_of_data_within_3_std_deviation = [result for result in hlist if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in wlist if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end] 
weight_list_of_data_within_2_std_deviation = [result for result in wlist if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end] 
weight_list_of_data_within_3_std_deviation = [result for result in wlist if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(hlist)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(hlist)))
print("{}% of data fr height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(hlist)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(wlist)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(wlist)))
print("{}% of data fr weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(wlist)))

