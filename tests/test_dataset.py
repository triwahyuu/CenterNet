import sys
import os
sys.path.append(os.path.join(os.path.abspath(""), "src/lib"))

from opts import opts
from datasets import get_dataset

if __name__ == "__main__":
    opt = opts().parse()
    Dataset = get_dataset(opt.dataset, opt.task)
    opt = opts().update_dataset_info_and_set_heads(opt, Dataset)

    data = Dataset(opt, 'train')
    d0 = data[2]
    print(len(data))