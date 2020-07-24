import argparse
from utils import *

def do_valid():
    return

def train(config):
    return

def validate(config):
    do_valid()
    return

def main(config):

    if config.mode == 'train':
        train(config)

    if config.mode == 'validate':
        with torch.no_grad():
            validate(config)

if __name__ == '__main__':
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = False
    torch.backends.cudnn.enabled = True

    def boolean_string(s):
        if s not in {'False', 'True'}:
            raise ValueError('Not a valid boolean string')
        return s == 'True'

    parser = argparse.ArgumentParser()
    parser.add_argument('--seven_mode', type=bool, default=False)
    parser.add_argument('--model', type=str, default='xx_net')
    parser.add_argument('--exp_name', type=str, default='exp0')
    parser.add_argument('--mode', type=str, default='train', choices=['train', 'val', 'infer'])

    config = parser.parse_args()
    main(config)
