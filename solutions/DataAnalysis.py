import numpy as np
import pickle as pkl
from scipy.stats import linregress

class DataAnalysis:
    """
    Data analysis class for Python seminar 2020.
    Written by Jens Hahn (27/05/2019)
    """
    def __init__(self, filename='../assignment_3/20190527_data.pkl'):
        """
        Initialise class variables
        """
        self.data = self.__load_data(filename)
        self.mean_list = self.__calculate_mean()
        self.median_list = self.__calculate_median()
        self.sd_list = self.__calculate_sd()
        self.normalised = False
        self.number_nans = self.__count_nans()

    def __load_data(self, filename):
        """
        Load data from pickled data
        """
        with open(filename, 'rb') as data_file:
            self.data = pkl.load(data_file)
        return self.data 
    
    def __count_nans(self):
        """
        Count all NaNs in the data set
        """
        self.number_nans = np.count_nonzero(np.isnan(self.data))
        return self.number_nans
    
    def __calculate_mean(self):
        """
        Calculate median of the data columns
        """
        mean_list = []
        for column_index in range(self.data.shape[1]):
            mean_list.append(np.nanmean(self.data[:, column_index]))
        return mean_list
            
    def __calculate_median(self):
        """
        Calculate mean of the data columns
        """
        median_list = []
        for column_index in range(self.data.shape[1]):
            median_list.append(np.nanmedian(self.data[:, column_index]))
        return median_list

    def __calculate_sd(self):
        """
        Calculate standard deviation of the data columns
        """
        sd_list = []
        for column_index in range(self.data.shape[1]):
            sd_list.append(np.nanstd(self.data[:, column_index]))
        return sd_list
    
    def normalise_rows(self):
        """
        Normalise the data to the highest value
        """
        for row_index in range(self.data.shape[0]):
            self.data[row_index, :] /= np.nanmax(self.data[row_index, :])
        self.normalised = True
     
    def interpolate_nans(self, row_index):
        """
        Interpolate linearly NaNs in the row
        """
        nan_indeces = []
        for column_index in range(self.data.shape[1]):
            if np.isnan([self.data[row_index, column_index]]) == True:
                nan_indeces.append(column_index)
        if nan_indeces:  # go only on if there are indeed NaNs 
            mask = ~np.isnan(self.data[row_index, :])
            x_val = range(0, self.data.shape[1])
            x_val = np.array(x_val)
            x_val = x_val[mask]
            interpolated_values = np.interp(nan_indeces, x_val, self.data[row_index, :][mask])
            for interpol_index, interpol_value in enumerate(interpolated_values):
                self.data[row_index, nan_indeces[interpol_index]] = interpol_value
    
    def linear_regression_row(self, row_index):
        """
        Perform linear regression on row
        """
        mask = ~np.isnan(self.data[row_index, :])
        x_val = np.array(range(self.data.shape[1]))[mask]
        slope, intercept, r_value, p_value, std_err = linregress(x_val, self.data[row_index,:][mask])
        return slope, intercept, r_value, p_value