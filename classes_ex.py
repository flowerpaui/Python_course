import data_class
analyse=data_class.DataAnalysis() #warum das doppelte, warum extra klasse???
analyse.import_data("20190527_data.pkl")

analyse.calc_mean(analyse.data)

analyse.calc_median(analyse.data)

analyse.calc_sd(analyse.data)

analyse.normalise(analyse.data)