%v16
%initialized date: 23 may 2022
%last updated: 25 may 2022
%energy efficiency of NOMA asynchronous D2D SIC decoding
%Output: Energy efficiency based ...
%on number of users in ...
%proposed optimized sic traingle decoding method
%testing complexity results: ee vs total interference in sic triangle
clc;
clear all;
close all;

%% input data: environmnet
%--------------------------------------------------------------------------
%%scalars
%number of users 
alldatadecoded = false;
mpriority = 20;
x = zeros(mpriority,1);
y = zeros(mpriority,1);
z = zeros(mpriority,1);
zz = zeros(mpriority,1);
e = zeros(mpriority,1);
f = zeros(mpriority,1);
g = zeros(mpriority,1);
h = zeros(mpriority,1);
i = zeros(mpriority,1);
j = zeros(mpriority,1);
%% 
% Number of Bits
N=10^4;  

communication_radius = 30;%change this 
max_dist     = 100;%meters
max_eta      = 15;
etath        = 4;%change this 
noisepower   = 0.1;
max_tx_power = 20;%change this
B            = 1;%channel bandwidth

pth          = max_tx_power.*communication_radius^-etath;
h_th         = sqrt(communication_radius^-etath)*sqrt(pth/2)*(randn(1,N)+...
1i*randn(1,N))/sqrt(2);
g_th         = (abs(h_th)).^2;

rate_th      = log2( 1 + sqrt(pth/2)*g_th/noisepower);

eth          = 1;
timeslot     = 1;

%random iterations
%--------------------------------------------------------------------------
userK_vec = [3,5,8,15,20];
K = 20;%number of superimposed data

for indx = 1:1:mpriority 
initialK = K;
%K = indx;
%Distances of users from rx
dist_k = max_dist*abs(randn(K,1));

%sorted transmit power vector %descending 
dist_vec = sort(dist_k,'ascend'); 

% Path loss exponent
eta_k   = max_eta*abs(randn(K,1));
eta_vec = sort(eta_k,'ascend'); 

% unsorted transmit power vector
transmitpow_k = max_tx_power*abs(randn(K,1));

%sorted transmit power vector %descending 
power_vec = sort(transmitpow_k,'descend'); 

%tx power vec
%power_vec = tx_power_percentage_vec.*tx_pow_k;
pathloss_exp = sqrt(dist_vec.^-eta_vec);

%channel coefficients of each user vec
h_vec =  pathloss_exp.*sqrt(power_vec/2).*(randn(1,N)+1i*randn(1,N))/sqrt(2);

%channel gains of each user vec
g_vec = (abs(h_vec)).^2;

%symbol interference vec
symdur_k = 1*abs(randn(K,1));
sym_dur_vec = sort(symdur_k,'descend');%change here

pr_vec = [0.5;1;1.5;2;2.5;3;3.5;4;4.5;5;5.5;6;6.5;7.5;8;8.5;10;12;15;20];

%rng(1);%same random seed
%fprintf("indx pr  %i %f\n",indx,pr_vec(indx));

[x(indx),y(indx),z(indx),zz(indx),e(indx),f(indx),g(indx),...
    h(indx),i(indx),j(indx)] =...
    seqsic(initialK,alldatadecoded,K,...
    pr_vec(2),power_vec,sym_dur_vec,g_vec,max_tx_power,timeslot,N,h_vec);
    z
    zz
    i
    j
end

save x.mat;
save y.mat;
save z.mat;
save zz.mat;

function [a,b,c,d,e,f,g,h,i,j] = seqsic(initialK,alldatadecoded,K,priority,power_vec,sym_dur_vec,...
g_vec,max_tx_power,timeslot,N,h_vec)

sim_delay_prop = 0;
sim_delay_conv = 0;
nbiterations=1;

for nbusers = initialK: initialK%number of superimposed data loop
for i = 1:100 %random iterations 
v =1;

while (alldatadecoded == false) 

%nsymbols vector of each user: K vec #loop
clear K_vec;
for k = 1:K
    K_vec(k,1) = K-(k-1);
end
initialK_vec = K_vec;

miter = 10;
priority_max = 30;
lambda1 = priority;%change this%energy saving priority %left energy is low
learn_rate = 0.4;
tolerance2 = 0.5;%lambda
tolerance = 0.02;%uk
Rmin = 1e-6;
sinr_th = 1e-6;

%--------------------------------------------------------------------------
%vectors
interf_vec     = zeros(K,1);
factorialk_vec = zeros(K,1);
sumsym_dur_vec = zeros(K,1);
desired_id   = 1;

for j = 1:K%interference vector loop
for k =1:K
    %interference vec %only from the next neighbor user
    if k ~= desired_id & k == desired_id+1
        
        interf_vec(desired_id,1) = power_vec(k)*1*sym_dur_vec(k)...
            + interf_vec(desired_id,1);
        sumsym_dur_vec(desired_id,1)= interf_vec(desired_id,1)...
            + sumsym_dur_vec(desired_id,1);
    end      
end
 desired_id = desired_id+1;
end
       
%% optimization problem
pastdelay = 0;
nbiter = 10;
noisepower   = 0.1;
if(K>1)
opt_decision_uk = 0.1*ones(K,1);
startlam = 7;
n_iter   = 30;
tolerance = 0.5;
lam = startlam;
grad_lam = 2*lam;
%K_vec = [3,2,1];
learn_rate = 0.1;

proptstart(v)=tic;

[convergedukfin,nbiterationslam,lam,nbiterationsuk,opt_decision_uk] = grad_descent_uklam(grad_lam,...
    lam,learn_rate,n_iter,tolerance,K_vec,opt_decision_uk,K);

%complexity prop
sic_complextiyprop(v) = sum(opt_decision_uk)^2*(1/tolerance)*(1/tolerance);

proptend(v)    = toc(proptstart(v));

K = K-sum(opt_decision_uk);%update K

%complexity analysis
%proptend(v) = toc(proptstart(v));

random_iterations = 10;
N=10^4;  

userdata_vec = rand(initialK,N)>0.5;          % Generation of data for user1
clear K_vec;
for k = 1:K
    K_vec(k,1) = length(opt_decision_uk)-(k-1);
end

%% sim delay

if(K>1)
    [sim_delay_prop(v),ber_prop(v)] = sim_delayfunc(K, h_vec(1:K,:), userdata_vec(1:K,:), random_iterations,K_vec);
end
if(K>1)
    [sim_delay_conv(v),ber_conv(v)] = sim_delayfunc(initialK, h_vec(1:initialK,:), userdata_vec, random_iterations,initialK_vec);
end

if K<=1 
    alldatadecoded = true;
    %proptend(v)    = toc(proptstart(v));
    disp('break');
    nbiterations  = nbiterations+1;
    iterations(v) = nbiterations;
else
    nbiterations  = nbiterations+1;
    iterations(v) = nbiterations;
    fprintf('nbiterations %i\n',nbiterations);
    %break;
end%end if 

end%end if 
end

%% throughput of each user
%considering synchronous uplink noma
E_max = 10;

SINR_k = power_vec(1:K).*mean(g_vec(1:K,:),2)./(interf_vec(1:K)+noisepower^2);

throughput_vec = log(1+SINR_k);

total_throughput = sum(throughput_vec);
total_throughput = 2;%fix here????
%% energy efficiency 
%proposed optimal sic
for k = 1:length(opt_decision_uk)
    K_vec(k,1) = length(opt_decision_uk)-(k-1);
end

total_energ_consump = E_max - E_max^(exp(-log(2)/1000*opt_decision_uk'*K_vec));
energy_eff(v) = total_throughput/(total_energ_consump +0.01);
energy_eff;

%%conv sic
total_energ_consump_conv = E_max - E_max^(exp(-log(2)/1000*sum(initialK_vec)));
energy_eff_conv(v) = total_throughput/(total_energ_consump_conv+0.01);
energy_eff_conv;
if(energy_eff_conv<0)
    pause on;
end

%complexity analysis
convtstart(v) = tic;
for l = 1: sum(initialK_vec)
   for g = 1:sum(initialK_vec) 
   end
end
convtend(v) = toc(convtstart(v));

%% complexity analysis 

%only sic decoding 
sic_complextiyconv(v) = sum(initialK)^2;


v = v+1;%all user decoding index v

end%end while
%i: random iteration index
avgenergy_eff(i) = abs(mean(energy_eff));
avgenergy_effconv(i) = abs(mean(energy_eff_conv));

avgcomplexity_prop(i) = mean(sic_complextiyprop);
avgcomplexity_conv(i) = mean(sic_complextiyconv);

avgdelay_conv(i) = mean(sim_delay_conv);
avgdelay_prop(i) = mean(sim_delay_prop);

%avgiterations = mean(propend);
totaldelay_prop(i) = mean(sim_delay_prop+iterations*0.01);
avggradientdelay(i) = mean(proptend);

avgberconv(i) = mean(ber_conv);
avgberprop(i) = mean(ber_prop);

end

a = abs(mean(energy_eff_conv));
b = abs(mean(energy_eff));

c = mean(sic_complextiyconv);
d = mean(avgcomplexity_prop);

e = mean(avgdelay_conv);
f = mean(avgdelay_prop);

g = mean(totaldelay_prop);
h = mean(avggradientdelay);

i = mean(avgberconv);
j = mean(avgberprop);

fprintf("nbusers %i\n",nbusers);
fprintf("avg energy eff proposed %f\n",mean(energy_eff));
fprintf("avg energy eff conv %f\n",mean(energy_eff_conv));
fprintf("complexity conv %f\n",mean(sic_complextiyconv));
fprintf("complexity prop %f\n",mean(sic_complextiyprop));

end

function [sim_delay,ber_mean] = sim_delayfunc(K, h_vec, userdata_vec, random_iterations, K_vec)

for i = 1: random_iterations%random iterations
proptstart(i) = tic; 

%superimposed data
super_signal = h_vec.*userdata_vec;

%AWGN noise 
noise= 1/sqrt(2)*[randn(K,length(super_signal)) + j*randn(K,length(super_signal))];

%received signal 
y = super_signal + noise; %Addition of Noise

%equalization 
eq_vec = y./h_vec;

est_sym = zeros(3,3);

for k = 1:size(eq_vec,1)
    K_vec(k,1) = size(eq_vec,1)-(k-1);
end

%sic decoding for each user symbol 
for nbsym = 1:size(eq_vec,1)
    if nbsym ==1
        est_sym(nbsym,:) = eq_vec(K_vec(nbsym),1:size(est_sym,1))>0;
    else
        sub_vec = sum(eq_vec(K_vec(1:nbsym),:),1:size(est_sym,1)) - ...
            sum(est_sym(1:nbsym-1,:),1:size(est_sym,1));
        est_sym(nbsym,:) = sub_vec>0;
    end
end

%ber analysis
%compare est symbol with the actual symbol
ber(i) = abs(mean(mean(est_sym - userdata_vec(:,1:3),2)));

propend(i) = toc(proptstart(i));
end
sim_delay  = mean(propend);
ber_mean = mean(ber);
end

function [convergedukfin,nbiterationslam,lam,nbiterationsuk,decision_uk] = grad_descent_uklam(grad_lam,...
    lam,learn_rate,n_iter,tolerance,K_vec,decision_uk,K)
    if K>5
        startlam = 1.15;
    else 
        startlam = 0.9;  
    end
    
    convergeduk = false;    
    convergedlam = false;   
    nbiterationslam = 1;
    nbiterationsuk  = 1;
    %decision_uk = [0.1,0.1,0.1];%initial
    %decision_uk = decision_uk>0.8
    while(convergedlam==false)
        grad_uk = -K_vec-lam...
                            + 2*lam'*decision_uk;
                        
        %fprintf('0 grad_uk %f\n',grad_uk)                
        diffuk  = -learn_rate*(grad_uk);
        %fprintf('1 diffuk %f\n',diffuk)     
        
        if (abs(diffuk)<= tolerance)
            convergeduk = true;
            nbiterationsuk = nbiterationsuk+1;
            
            while(convergeduk == true)
                grad_lam = -sum(decision_uk)...
                + sum(decision_uk.^2);
                diff = -learn_rate*grad_lam;

                if (abs(diff)<= tolerance)
                    converged_lam = lam;
                    nbiterationslam = nbiterationslam+1;
                    %disp('yea')
                    convergedlam = true;
                    convergeduk = false;   
                    convergedukfin = true;
                    %fprintf('decision_uk %f\n',decision_uk)
                    decision_uk =decision_uk>0.8;
                else
                    converged_lam = 0;
                    nbiterationslam = nbiterationslam+1;
                    lam = lam + diff;
                    %fprintf('lam: %f\n',lam);
                end               
            end            
        else
            decision_uk    = decision_uk + diffuk;
            %decision_uk = decision_uk>0.8
            if ((decision_uk) <zeros(K,1))
                 decision_uk = zeros(K,1);
            end
            nbiterationsuk = nbiterationsuk+1;
        end
       
    end   
     
end