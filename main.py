import imageio
import os
import numpy as np
import cv2
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import mpm
import utils
from PIL import Image
import modules
import time
import argparse
import matlab.engine
import matplotlib.pyplot as plt
myparser = argparse.ArgumentParser()
myparser.add_argument('--input', type=str, dest="input",
                      default=r'dataset\test_set')
myparser.add_argument('--output', type=str, dest="output",
                      default=r'dataset\test_out')
myparser.add_argument('--pretrain', type=str, dest="weight_model",
                      default=r'checkpoint\AOAF_model.pth')

args = myparser.parse_args()


# set path 
test_path = args.input
save_path = args.output


if __name__ == "__main__":
    #read file
    testx = utils.readfile(args.input)
    data_num = testx.shape[0]
    eng = matlab.engine.start_matlab()
    # set model
    train_transform = transforms.Compose([transforms.ToTensor()])
    test_set = modules.imgdataset(testx, None, train_transform)
    test_loader = modules.DataLoader(test_set, batch_size=1, shuffle=False)
    
    model_test = modules.Denoise_conv().cuda()
    model_test.load_state_dict(torch.load(args.weight_model))
    model_test.eval()

    # test 
    save_array = np.ones([data_num, 1, 512, 512], dtype='uint8')
    with torch.no_grad():
        for i, data in enumerate(test_loader):
            AOAF_Results = eng.AOAF(matlab.double(data.numpy().reshape(512,512).tolist()))
            AOAF_Results = torch.from_numpy(np.asarray(AOAF_Results).reshape(1 , 1 , 512 , 512)).float()
            #plt.imsave(rf'D:\Users\Admin\Downloads\OAF_code\dataset\AOAF_Results\{i}.png' , aa, cmap = 'gray') 
            #print(data.numpy().shape)
            start = time.time()
            test_pred = model_test(AOAF_Results.cuda())
            end = time.time()
            out_np = test_pred.detach().cpu().numpy()
            save_array[i] = out_np

    #save image
    save_array = np.transpose(save_array, (0, 2, 3, 1))
    utils.savefile(save_array, save_path, test_path)
