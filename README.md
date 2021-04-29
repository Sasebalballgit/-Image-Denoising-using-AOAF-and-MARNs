# Image Denoising using Adaptive and Overlapped Average Filtering and Mixed-pooling Attention Refinement Networks  

**Ming-Hao Lin, Zhi-Xiang Hou, Kai-Han Cheng, Chin-Hsien Wu, and Yan-Tsung Peng** <br>
<br>
## **Abstract:** <br>

_Cameras have been essential parts of portable devices, such as smartphones and tablets.
Most people have a smartphone and can take pictures anywhere, anytime to record their lives.
However, these pictures captured by cameras may suffer from noise contamination, causing issues for
subsequent image analysis, such as image recognition, object tracking, and classification of an object in
the image. This paper develops an effective combinational denoising framework based on proposed
Adaptive and Overlapped Average Filtering (AOAF) and Mixed-pooling Attention Refinement
Networks (MARNs). First, we apply AOAF to the noisy input image to obtain a preliminarily
denoised result, where noisy pixels are removed and recovered. Next, MARNs take the preliminary
result as the input and output a refined image where details and edges are better reconstructed.
The experimental results demonstrate that our method performs favorably against state-of-the-art
denoising methods._

## Highlights <br>
![image](https://github.com/Sasebalballgit/Image-Denoising-using-Adaptive-and-Overlapped-Average-Filtering-and-Mixed-pooling-Attention-Refineme/blob/main/Example/r_gray_com.png)
Examples of denoising results using different methods. (a) Original Image. (b) Images with50% ,60%,70%,80%, 90% noise added. Denoising results using (c) MDBUTMF, (d) DAMF,  (e) FASMF, and (f) MMAP, (g) the proposed (AOAF+MARNs).

## Environment <br>
*  Platforms: Windows 10  / cuda 11.0 <br>
*  python: 3.8.0 / pytorch: 1.7.0 <br>
*  matlab: R2020a <br>
*  **Additional Requirements:** MATLAB Engine <br>
## Quick Start <br>
<h3> 1. Install MATLAB Engine API for Python (for OAF_Concat version)</h3>


To install the engine, You must run the following commands via the MATLAB command prompt <br>

```
"cd (fullfile(matlabroot,'extern','engines','python'))"
"system('python setup.py install')"
```

(you may need administrator privileges to execute these commands) <br>

<h3> 2. Testing </h3>

  *AOAF_test1*
* To reproduce the experimental results reported in the paper, please run the following script <br>
  * `Execute AOAF_single.m` <br>
  * `python main_single.py --input=dataset/test_set --output=dataset/test_set --pretrain=checkpoint/AOAF_model.pth` <br>
  
 *AOAF_test2*
 
* We also release an integrated version, which bears an ignorable and invisiable difference against AOAF_test1. Plesae run <br>
  * `python main.py --input=dataset/test_set --output=dataset/test_set --pretrain=checkpoint/AOAF_model.pth` <br> <br>
