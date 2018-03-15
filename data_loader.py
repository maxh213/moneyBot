import csv
import random

class Employee:
       'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

class DataLoader:

    def __init__(self):
        self.doge_data = []
        self.training_data = []
        self.testing_data = []
        self.TRAINING_DATA_SIZE = 5
        self.TRAINING_DATA_RESULT_SIZE = 1
        self.DATA_SEGMENT_SIZE = self.TRAINING_DATA_SIZE+self.TRAINING_DATA_RESULT_SIZE

    def load_file(self):
        with open('doge-usd-max.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.doge_data.append([row['price'], row['market_cap'], row['total_volume']])

    def set_Up_Data_Ready_For_The_NN(self):
        self.set_training_data()
        random.shuffle(self.training_data)
        self.set_testing_data()
        
    def set_training_data(self):
        for i in range(len(self.doge_data)-self.DATA_SEGMENT_SIZE)
            data_set = self.get_next_data_set(i, self.doge_data)
            self.training_data.append(data_set)

    def get_next_data_set(self, i, data):
        output = []        
        for j in range(self.DATA_SEGMENT_SIZE):
            output.append(data[i+j])
        return [output[:self.TRAINING_DATA_SIZE], output[-self.TRAINING_DATA_RESULT_SIZE:]]   

    def set_testing_data(self):
        self.testing_data = self.training_data[-250:]
        self.training_data = self.training_data[:1300]   

if __name__ == "__main__":
    dataLoader = DataLoader()