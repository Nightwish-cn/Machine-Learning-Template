import sys
sys.path.append("../..")
from includes import *

class Dataset_XXX(Dataset):
    def __init__(self, fold_index=0,
                 multi_res = False):
        super(Dataset_XXX, self).__init__()
        print('fold '+ str(fold_index))

    def set_aug(self, augment):
        self.augment = augment

    def set_mode(self, mode):
        self.mode = mode

        if self.mode == 'train':
            print("set dataset mode: train")

        elif self.mode == 'valid':
            print("set dataset mode: valid")

        elif self.mode == 'test':
            print("set dataset mode: valid")

    def __getitem__(self, index):
        return None

    def __len__(self):
        return self.num_data

def run_check_train_data():
    dataset = CASPDataset_mrf(mode = 'train')
    num = len(dataset)

def run_check_valid_data():
    dataset = CASPDataset_mrf(mode = 'valid')
    num = len(dataset)

if __name__=='__main__':
    run_check_train_data()
    run_check_valid_data()


