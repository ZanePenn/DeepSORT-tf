from configuration import Config

class DetectionDataset:
    def __init__(self):
        self.txt_gt = Config.txt_gt
        self.batch_size = Config.batch_size
    
    @staticmethod
    def __get_length_of_dataset(dataset):
        return dataset.