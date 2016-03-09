clc;
clear;
%format short g;
NumOfTimes=30;
NumOfColumns=3000;
A=load('male_day_3.mat');
Data_ch1=A.lat_ch1';
Data_ch2=A.lat_ch2';
for n=1:NumOfTimes
    tempData(:,1)=Data_ch1(:,n);
    tempData(:,2)=Data_ch2(:,n);
    tempName=strcat('male_day_2_lat_',num2str(n),'.txt');
    %save(tempName,'tempData','-ASCII');
    dlmwrite(tempName,tempData,'delimiter','\t','precision','%0.5f');
    clear tempData;
end
