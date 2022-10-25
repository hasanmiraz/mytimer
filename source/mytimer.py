from datetime import datetime
import pickle

class MyTimer:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.stop_time = None

    def start_t(self):
        self.start_time = datetime.now()


    def stop_t(self):
        self.stop_time = datetime.now()

    def debug_data(self):
        print("debugging: ")
        print(self.name)
        print(self.start_time)
        print(self.stop_time)

    def write_t(data_list):
        for i in data_list:
            i.stop_t()

        with open('data.pkl','wb') as file:
            pickle.dump(data_list, file)

    def read_t():
        with open('data.pkl', 'rb') as file:
            return pickle.load(file)