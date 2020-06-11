class DataAnalysis: 
    def import_data(self,filename):
        import pickle as pkl
        self.path=str("./assignment_data/"+filename) #where are the datasets
        with open(self.path, "rb") as self.data_file:
            self.data = pkl.load(self.data_file) #open
        return self.data #do i need this??????

    def calc_mean(self, dataset):
        import numpy as np #why unable??
        meantype=input("Which mean do you want? The mean of all your data (answer 1) seperate means for every experiment(answer 2)?")
        if meantype == "1":
            self.allmean=np.nanmean(dataset)
            print(self.allmean, "(if you want to work with this value, assess it via \"[].allmean\")")
            return 
        if meantype == "2":
            self.rowmeans=[]
            for col_ind in range(dataset.shape[1]):
                self.rowmeans.append(np.nanmean(dataset[:,col_ind]))
            print(self.rowmeans, "(if you want to work with these values, assess them via \"[].rowmeans\")")
            return 
        else:
            print("choose a mean type.")

    def calc_median(self, dataset):
        import numpy as np 
        meantype=input("Which median do you want? The median of all your data (answer 1) seperate medians for every experiment(answer 2)?")
        if meantype == "1":
            self.allmed=np.nanmedian(dataset)
            print(self.allmed, "(if you want to work with this value, assess it via \"[].allmed\")")            
            return
        if meantype == "2":
            self.rowmeds=[]
            for col_ind in range(dataset.shape[1]):
                self.rowmeds.append(np.nanmedian(dataset[:,col_ind]))
            print(self.rowmeds, "(if you want to work with these values, assess them via \"[].rowmeds\")")            
            return 
        else:
            print("choose a median type.")     

    def calc_sd(self, dataset):
        import numpy as np 
        meantype=input("Which standard deviation do you want? The sd of all your data (answer 1) seperate sds for every experiment(answer 2)?")
        if meantype == "1":
            self.allsd=np.nanmean(dataset)
            print(self.allsd, "(if you want to work with this value, assess it via \"[].allsd\")")
            return
        if meantype == "2":
            self.rowsds=[]
            for col_ind in range(dataset.shape[1]):
                self.rowsds.append(np.nanstd(dataset[:,col_ind]))
            print(self.rowsds, "(if you want to work with these values, assess them via \"[].rowsds\")")
        else:
            print("choose an sd type.")  

    def normalise(self, dataset):
        import numpy as np 
        meantype=input("How do you want to normalise? On the maximum of all your data(1) or the single experiments'(2)?")
        if meantype == "1":
            self.allnormdat= dataset/np.nanmax(dataset)
            print("if you want to work with this dataset, assess it via \"[].allnormdat\")")
            return
        if meantype == "2":
            self.rowsnormdat=[]
            for row_ind in range(dataset.shape[0]):
                self.rowsnormdat=dataset[row_ind,:]/np.nanmax(dataset[row_ind,:])
            print("if you want to work with these values, assess them via \"[].rowsnormdat\")")
        else:
            print("choose a normalisation type.") 

