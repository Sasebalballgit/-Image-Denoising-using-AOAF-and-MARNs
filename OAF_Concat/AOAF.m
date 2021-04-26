function I_aoaf = AOAF( I  )

%         tic;
        I = double( I );
       
        [ M, N ] = size( I ) ;

        B = zeros( M , N );
        B( (I > 0 ) & ( I < 1 )) = 1;
        
        L = 19;

        padimg = padarray( I , [ L L ] , 'symmetric', 'both' );
        
        B = padarray( B , [ L L ] , 'symmetric', 'both' );
      
        [rows, cols] = size( padimg );
     
       
     
        C = B ;
        T = B.*padarray( I , [ L L ] , 'symmetric', 'both' ); % B\otimes I
       

        for j = L+1 : rows-L 
          
            for k = L+1 : cols-L         
                if (B(j,k) == 0)
                    r = 1;     %r is initialized to be 1 in Find_Kernel_Radius
                    low = -r ; high = r ; cond = 1 ;  
                    while (cond == 1 )
                        p = 1 ;
                      
                        for m=low : high
                            for n=low : high
                                y(p) = padimg( j + m , k + n );  
                                p = p + 1 ; 
                            end
                        end
                       
                        good = find((y>0) & (y<1)); 
                        [~,c] = size(good);
                     
                        if ( c >= 1 ) 
                            for m = low : 1 : high
                                for n = low : 1 : high
                                    if( padimg( j + m , k + n ) == 0 || padimg( j + m , k + n ) == 1 ) 
                                        T( j + m , k + n ) = T( j + m , k + n ) + mean( y(good ) )  ;     %replaced by weighted of good pixels
                                        C(j + m , k + n ) = C( j + m , k + n ) + 1 ; 
                                    end
                                end
                            end
                            
                            cond = 0 ;
                        else                    %if we did not reach the maximum radius and not find non-noisy pixels, r is increased by 1
                            r   = r+1;          %Find_Kernel_Radius
                            low = -r;
                            high = r ;
                         
                                if (high > L ) 
                        
                                  T( j , k ) = T( j , k ) +  mean( y ); 
                                  C( j , k ) = C( j , k ) + 1 ; 
                                  cond = 0 ; 
                                end
                        end
                      
                       
                        clear y; 
                        clear good;
                    end
                end
            end
        end

        I_aoaf = (T(L+1 : rows-L, L+1 : cols-L) ./ C(L+1 : rows-L, L+1 : cols-L));
       % imwrite(uint8( I_aoaf) .* 255.0  , "D:\Users\Admin\Downloads\OAF_code\dataset\AOAF_Results\GVDFSGEASG.png"); 
end