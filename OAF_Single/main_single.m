clc ; 
clear ; 
  
imgRoot = './test/';
outRoot = './tmp_result/';
addpath(imgRoot); 
addpath(outRoot);
dpath = [dir([imgRoot '*' 'bmp']) ; dir([imgRoot '*' 'jpg']) ; dir([imgRoot '*' 'png']) ; ]; 
dpath_2 = [dir([outRoot '*' 'bmp']) ; dir([outRoot '*' 'jpg']) ; dir([outRoot '*' 'png']) ; ]; 
for i = 1 : 1 : length( dpath )
    %tic;
    cd('./test') ; 
    input_img  = imread(dpath(i).name ); 
 
    cd('..');
    output_img = AOAF( input_img) ;  
    
    
    imwrite(( output_img) , sprintf('%s%s%s', outRoot, dpath(i).name,"_denoised.bmp" ));  
   
    
    %time=toc;
    %disp(time) ;
    
end



