%ref:https://in.mathworks.com/matlabcentral/fileexchange/23498-mc-cdma
clc;
close all;
clear all;
k1=5; %Rician factor %ref: https://www.researchgate.net/publication/263669548_Probability_Distribution_of_Rician_K-Factor_in_Urban_Suburban_and_Rural_Areas_Using_Real-World_Captured_Data
mean=sqrt(k1/(k1+1));% mean
sigma=sqrt(1/(2*(k1+1)));%variance
N=10^3;  % Number of Bits for data_user1
d1 = 0.8; d2 = 500;    %Distances of users from base station (BS)
d3 = 5;d4 = 5;d5 = 5;d6 = 5;d7 = 5;d8 = 5;d9 = 5;dA=0.8;
eta = 4;            %Path loss exponent

%% ------------------Hop 1------------------------------
users=1;            % Number of Users
%------------------Generation of Walsh code--------------------------------
n =64;                               %Number of  Data Sub-Carriers
walsh=hadamard(n);              
code1=walsh(2,:);                   %Taking 2nd row of walsh code for User1
code4=walsh(1,:);                   %Taking 2nd row of walsh code for User1
code2=walsh(4,:);   
code3=walsh(3,:); %Taking 3rd row of walsh code for User2
code5=walsh(5,:); 
code6=walsh(6,:); 
code7=walsh(7,:); 
code8=walsh(8,:); 
code9=walsh(9,:); 
codeA = walsh(10,:); 
codeB = walsh(11,:); 
codeC = walsh(12,:); 
codeD = walsh(13,:); 
codeE = walsh(14,:); 
codeF = walsh(15,:); 

%------------------Generating data for User1-------------------------------                     
data_user1 = rand(1,N)>0.5;          % Generation of data for user1
data_user1bpsk = 2*data_user1-1;    % BPSK modulation 0 -> -1; 1 -> 0 

%------------------Spreading & IFFT for User1------------------------------
data_user11=data_user1bpsk';
spdata1_user1=data_user11*code1;    % Spreading 
spdata12=(spdata1_user1)';
ifftdata_user1=ifft(spdata12);      % Taking the IFFT
ifftdata12=ifftdata_user1';

%------------------Append Cyclic Prefix1 for User1-------------------------
y1=[ifftdata12(:,[(n-2):n]) ifftdata12];
transdata1=y1';
tx_user1=transdata1;                % Transmitting data for user1

%----------------------Adding data for Transmission of All User------------
x=tx_user1;
%----------------------Creating Rayleigh Channel---------------------------
Taps=4;                                        % Number of Taps
p1=1;                                       % Power of Tap1
p2=1;                                     % Power of Tap2
p3=1;                                     % Power of Tap3
p4=1;
gain1=sqrt(d1^-eta)*sqrt(p1/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap1
ch1=repmat(gain1,(n+3),1);     
data_channel1=sqrt(d1^-eta)*sqrt(p1/2)*x;  % Passing data through channel 

%% ------user 2 using same code but different channel
                  %Taking 2nd row of walsh code for User1
%------------------Generating data for User1-------------------------------                          
data_user2= rand(1,N)>0.5;          % Generation of data for user1
data_user2bpsk = 2*data_user2-1;    % BPSK modulation 0 -> -1; 1 -> 0 

%------------------Spreading & IFFT for User1------------------------------
data_user22=data_user2bpsk';
spdata1_user2=data_user22*code1;    % Spreading 
spdata122=(spdata1_user2)';
ifftdata_user2=ifft(spdata122);      % Taking the IFFT
ifftdata122=ifftdata_user2';

%------------------Append Cyclic Prefix1 for User1-------------------------
y2=[ifftdata122(:,[(n-2):n]) ifftdata122];
transdata2=y2';
tx_user2=transdata2;                % Transmitting data for user1

%----------------------Adding data for Transmission of All User------------
x2=tx_user2;
%----------------------Creating Rayleigh Channel---------------------------
Taps=4;                                        % Number of Taps
gain1s=sqrt(d2^-eta)*sqrt(p1/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap1
gain2s=sqrt(p2/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap2
gain3s=sqrt(p3/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap3
gain4s=sqrt(p4/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap4
x110=x2(:);
x120=reshape(x110,1,length(x110));
i=1:length(x120);        
delay1=1; 
for i=delay1+1:length(x120) % Producing one sample delay in Tap2 w.r.t. Tap1
   x13(i)=x2(i-delay1);
end
delay2=2;
for i=delay2+1:length(x120) % Producing two sample delay in Tap2 w.r.t. Tap1
   x14(i)=x2(i-delay2);
end
delay3=3;
for i=delay3+1:length(x120) % Producing three sample delay in Tap2 w.r.t. Tap1
   x15(i)=x2(i-delay3);
end
x111=reshape(x13,(n+3),length(x13)/(n+3));
x222=reshape(x14,(n+3),length(x14)/(n+3));
x333=reshape(x15,(n+3),length(x15)/(n+3));
ch11=repmat(gain1s,(n+3),1);     
ch22=repmat(gain2s,(n+3),1);
ch33=repmat(gain3s,(n+3),1);
ch44=repmat(gain4s,(n+3),1);
data_channel2=x2.*ch11+x111.*ch22+x222.*ch33+x333.*ch44;  % Passing data through channel 

%------------------------Addition of AWGN noise ---------------------------
data_channel = data_channel1+ data_channel2;
data_noise=data_channel(:);
data_noise=reshape(data_noise,1,length(data_noise));
noise = 1/sqrt(2)*[randn(1,length(data_noise)) + j*randn(1,length(data_noise))]; 

%% ------ receiver ---------------------
snr = [0:20];                 % multiple Eb/N0 values

for i = 1:length(snr)
y2= data_noise + (sqrt(1)*10^(-snr(i)/20))*noise; %Addition of Noise
  
%--------------------------Receiver ---------------------------------------
data_received2 = y2;           %fadded data received with awgn noise
%---------------------Removing Cyclic Prefix-------------------------------
rx1=reshape(data_received2,(n+3),length(data_received2)/(n+3));
rx12=rx1';
rx13 = rx12(:,[(4:(n+3))]); 
rx14=rx13';

%-----------------Taking FFT ----------------------------------------------
fft_data_received2 =fft(rx14);

%----------------equilization of the channel-------------------------------
data_equilized1=fft_data_received2;

channel_response2=fft([gain1s;gain2s;gain3s;gain4s],n);
data_equilized2=fft_data_received2.*conj(channel_response2);

%----------------BER of Data User1-----------------------------------------
recdata112=(data_equilized2'*code1')';
x11_hat = ones(1,N);
x11_hat(recdata112<0) = -1;
recdata11=(data_equilized1'*code1'-x11_hat')';
recdata12=real(recdata11)>0;
errors_user1(i) = size(find([data_user1- recdata12]),2); %Errors for User1
SBer1 = errors_user1/N;                              % simulated ber user1
                             
% simulated ber user2
% sic decoding
x12_hat = ones(1,N);
x12_hat(recdata11<0) = -1;
%recdata22=((data_equilized2'*code1') - x12_hat')';
recdata22=(data_equilized2'*code1' - x12_hat')';
recdata122=real(recdata22)>0;
errors_user2(i) = size(find([data_user2- recdata122]),2); %Errors for User1
SBer2 = errors_user2/N;                              % simulated ber user1
end

%% ------------------Hop 2------------------------------

users=2;            % Number of Users
%------------------Generation of Walsh code--------------------------------
estdata_user11bpsk = 2*recdata12-1;    % BPSK modulation 0 -> -1; 1 -> 0 
estdata_user11=estdata_user11bpsk';
spdata1_user11=estdata_user11*code1;    % Spreading 
spdata11=(spdata1_user11)';
ifftdata_user11=ifft(spdata11);      % Taking the IFFT
ifftdata11=ifftdata_user11';
y11=[ifftdata11(:,[(n-2):n]) ifftdata11];
transdata11=y11';
esttx_user11=transdata11;                

%------------------est for User12-------------------------------
estdata_user12bpsk = 2*recdata122-1;    % BPSK modulation 0 -> -1; 1 -> 0 
estdata_user12=estdata_user12bpsk';
spdata1_user12=estdata_user12*code3;    % Spreading 
spdata12=(spdata1_user12)';
ifftdata_user12=ifft(spdata12);      % Taking the IFFT
ifftdata12=ifftdata_user12';
y12=[ifftdata12(:,[(n-2):n]) ifftdata12];
transdata12=y12';
esttx_user12=transdata12;              

%------------------Generating data for User2-------------------------------
M=N;                             % Number of Bits for  data_user2
data_user3= rand(1,M)>0.5;          % Generation of data for user2
data_user2bpsk = 2*data_user3-1;    % BPSK modulation 0 -> -1; 1 -> 0 
data_user21=data_user2bpsk';
spdata2=data_user21*code2;          % Spreading 
spdata22=(spdata2)';
ifftdata_user2=ifft(spdata22);      % Taking the IFFT
ifftdata22=ifftdata_user2';
y2=[ifftdata22(:,[(n-2):n]) ifftdata22];
transdata2=y2';
tx_user2=transdata2;                % Transmitting data for user2

%----------------------Adding data for Transmission of All User------------
x3=esttx_user11+esttx_user12+tx_user2;
%----------------------Creating a new Rayleigh Channel---------------------------
p1=1;                                       % Power of Tap1
p2=1;                                     % Power of Tap2
p3=1;                                     % Power of Tap3
p4=1;
gain1ss=sqrt(d3^-eta)*sqrt(p1/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap1
gain2ss=sqrt(p2/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap2
gain3ss=sqrt(p3/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap3
gain4ss=sqrt(p4/2)*[randn(1,N)*sigma+mean + j*randn(1,N)*sigma];   % Gain for Tap4
x111=x3(:);
x122=reshape(x111,1,length(x111));
i=1:length(x122);        
delay1=1; 
for i=delay1+1:length(x122) % Producing one sample delay in Tap2 w.r.t. Tap1
   x133(i)=x3(i-delay1);
end
delay2=2;
for i=delay2+1:length(x122) % Producing two sample delay in Tap2 w.r.t. Tap1
   x144(i)=x3(i-delay2);
end
delay3=3;
for i=delay3+1:length(x122) % Producing three sample delay in Tap2 w.r.t. Tap1
   x155(i)=x3(i-delay3);
end
x11=reshape(x133,(n+3),length(x133)/(n+3));
x22=reshape(x144,(n+3),length(x144)/(n+3));
x33=reshape(x155,(n+3),length(x155)/(n+3));
ch11=repmat(gain1ss,(n+3),1);     
ch22=repmat(gain2ss,(n+3),1);
ch33=repmat(gain3ss,(n+3),1);
ch44=repmat(gain4ss,(n+3),1);
data_channel2=x3.*ch11+x11.*ch22+x22.*ch33+x33.*ch44;  % Passing data through channel 

%% ------user A using same code (code 2) but different channel

%original data for A                            % Number of Bits for  data_user2
data_userA= rand(1,M)>0.5;          % Generation of data for user2
data_userAbpsk = 2*data_userA-1;    % BPSK modulation 0 -> -1; 1 -> 0 
data_userAh2=data_userAbpsk';
spdataAh2=data_userAh2*code2;          % Spreading 
spdataAh2t=(spdataAh2)';
ifftdata_userAh2=ifft(spdataAh2t);      % Taking the IFFT
ifftdataAh2=ifftdata_userAh2';
yA=[ifftdataAh2(:,[(n-2):n]) ifftdataAh2];
transdataAh2=yA';
tx_userA=transdataAh2; 

%----------------------Adding data for Transmission of All User------------
xA=tx_userA;
%----------------------Creating a new Rayleigh Channel---------------------------
Taps=4;                                        % Number of Taps
data_channelA=sqrt(dA^-eta)*sqrt(p1/2)*xA;  % Passing data through channel 

data_channelhop2 = data_channel2+data_channelA;

%------------------------Addition of AWGN noise ---------------------------
data_noise2=data_channelhop2(:);
data_noise22=reshape(data_noise2,1,length(data_noise2));
noise22 = 1/sqrt(2)*[randn(1,length(data_noise22)) + j*randn(1,length(data_noise22))]; 
               
for i = 1:length(snr)
y2 = data_noise22 + (sqrt(1)*10^(-snr(i)/20))*noise22; %Addition of Noise
  
%--------------------------Receiver ---------------------------------------
data_received2 =y2;           %fadded data received with awgn noise
%---------------------Removing Cyclic Prefix-------------------------------
rx1=reshape(data_received2,(n+3),length(data_received2)/(n+3));
rx12=rx1';
rx13 = rx12(:,[(4:(n+3))]); 
rx14=rx13';

%-----------------Taking FFT ----------------------------------------------
fft_data_receivedhop2 =fft(rx14);
%----------------equilization of the channel-------------------------------
channel_response22=fft([gain1ss;gain2ss;gain3ss;gain4ss],n);
data_equilized22=fft_data_receivedhop2.*conj(channel_response22);

data_equilizedA=fft_data_receivedhop2/(sqrt(dA^-eta)*sqrt(p1/2));

%----------------BER of Data User1-----------------------------------------
recdata11=(data_equilized22'*code1')';
est1h1=real(recdata11)>0;
errors_user11(i) = size(find([data_user1- est1h1]),2); %Errors for User1
SBer11 = errors_user11/N;                              % simulated ber user1

%----------------BER of Data source User2-----------------------------------------
recdata12=(data_equilized22'*code3')';
est2h1=real(recdata12)>0;
errors_user12(i) = size(find([data_user2- est2h1]),2); %Errors for User1
SBer12 = errors_user12/N;                              % simulated ber user1

%----------------BER of Data relay User3-----------------------------------------
recdata3A=(data_equilizedA'*code2')';
xA_hat = ones(1,N);
xA_hat(recdata3A<0) = -1;
recdata3user=(data_equilized22'*code2'-xA_hat')';
est3h1=real(recdata3user)>0;
errors_user3(i) = size(find([data_user3- est3h1]),2); %Errors for User1
SBer3_user = errors_user3/N;     

%----------------BER of Data UserA-----------------------------------------
x3user_hat = ones(1,N);
x3user_hat(recdata3user<0) = -1;
recdataA=(data_equilizedA'*code2'-x3user_hat')';
estAh1=real(recdataA)>0;
errors_userA(i) = size(find([data_userA- estAh1]),2); %Errors for User1
SBerA = errors_userA/N;                              % simulated ber user1
                             
end

%hop3
[data_user4,data_userB,SBer1hop3,SBer2hop3,SBer3hop3,SBerAhop3,SBer4hop3,SBerBhop3,est1,...
    est2,est3,estA,est4,estB]=hop3(est1h1,...
    est2h1,est3h1,estAh1,code1,code2,code3,codeA,...
    code4,n,N,d4,eta,p1,sigma,mean,dA,snr,data_user1,data_user2,data_user3,data_userA);

%hop4
[data_user5,data_userC,SBer1h4,SBer2h4,SBer3h4,SBerAh4,SBer4h4,SBerBh4,...
    SBer5h4,SBerCh4,est1h4,est2h4,est3h4,estAh4,est4h4,estBh4,est5h4,estCh4]=hop4(est1,...
    est2,est3,estA,est4,estB,code1,code2,code3,codeA,...
    code4,codeB,code5,codeC,n,N,d4,eta,p1,sigma,mean,dA,snr,data_user1,data_user2,...
    data_user3,data_userA,data_user4,data_userB);

%hop5
[data_user6,data_userD,SBer1h5,SBer2h5,SBer3h5,SBerAh5,SBer4h5,SBerBh5,...
    SBer5h5,SBerCh5,SBer6h5,SBerDh5,est1h5,est2h5,est3h5,estAh5,est4h5,estBh5,est5h5,estCh5,...
    est6h5,estDh5]=hop5(est1h4,est2h4,est3h4,estAh4,est4h4,estBh4,est5h4,estCh4,code1,code2,code3,codeA,...
    code4,codeB,code5,codeC,code6,codeD,n,N,d6,eta,p1,sigma,mean,dA,snr,data_user1,data_user2,...
    data_user3,data_userA,data_user4,data_userB,data_user5,data_userC);

%hop6
[data_user7,data_userE,SBer1h6,SBer2h6,SBer3h6,SBerAh6,SBer4h6,SBerBh6,...
    SBer5h6,SBerCh6,SBer6h6,SBerDh6,SBer7h6,SBerEh6,est1h6,est2h6,est3h6,estAh6,est4h6,estBh6,est5h6,estCh6,...
    est6h6,estDh6,est7h6,estEh6]=hop6(est1h5,est2h5,est3h5,estAh5,est4h5,estBh5,est5h5,estCh5,...
    est6h5,estDh5,code1,code2,code3,codeA,...
    code4,codeB,code5,codeC,code6,codeD,code7,codeE,n,N,d4,eta,p1,sigma,mean,dA,snr,data_user1,data_user2,...
    data_user3,data_userA,data_user4,data_userB,data_user5,data_userC,data_user6,data_userD);

%hop7
[averagedelay,data_user8,data_userF,SBer1h7,SBer2h7,SBer3h7,SBerAh7,SBer4h7,SBerBh7,...
    SBer5h7,SBerCh7,SBer6h7,SBerDh7,SBer7h7,SBerEh7,SBer8h7,SBerFh7,est1h6,est2h6,est3h6,estAh6,est4h6,estBh6,est5h6,estCh6,...
    est6h6,estDh6,est7h6,estEh6,est8h7,estFh7]=hop7(est1h6,est2h6,est3h6,estAh6,est4h6,estBh6,est5h6,estCh6,...
    est6h6,estDh6,est7h6,estEh6,code1,code2,code3,codeA,...
    code4,codeB,code5,codeC,code6,codeD,code7,codeE,code8,codeF,n,N,d4,eta,p1,sigma,mean,dA,snr,data_user1,data_user2,...
    data_user3,data_userA,data_user4,data_userB,data_user5,data_userC,data_user6,data_userD,data_user7,data_userE);

fprintf('%f\n',averagedelay);
