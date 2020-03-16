%The ; denotes we are going back to new row
A = [1,2,3,4;5,6,7,8;9,10,11,12]
%Initialize a vector
v = [2;3;4]
%Get the dimension of the matrix A(m represents rows and n represents columns)
[m,n] = size(A)
%Alternatively
dim_A = size(A)
dim_v = size(v)
%Index into the 2nd row 3rd column of matrix A
A_23 = A(2,3)

