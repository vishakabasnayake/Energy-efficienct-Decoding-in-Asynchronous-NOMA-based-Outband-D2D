%v16
%last update: 14 june 2022

% %energy efficiency of NOMA asynchronous D2D SIC decoding
%Output: Energy efficiency based ...
%on number of users in ...
%proposed optimized sic traingle decoding method
%testing complexity results: ber vs nbdata
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
r = zeros(mpriority,1);
s = zeros(mpriority,1);
uu = zeros(mpriority,1);
vv = zeros(mpriority,1);
pp = zeros(mpriority,1);
ll = zeros(mpriority,1);
%% 
% Number of Bits
N=10^4;  

communication_radius = 30;%change this 
max_dist     = 100;%meters
max_eta      = 15;
etath        = 4;%change this 
noisepower   = 0.1;
max_tx_power = 500;%change this
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

for indx = 2:mpriority
initialK = indx;
K  = indx;

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
symdur_k = 0.5*abs(randn(K,1));
sym_dur_vec = sort(symdur_k,'descend');%change here

pr_vec = [0.5;1;1.5;2;2.5;3;3.5;4;4.5;5;5.5;6;6.5;7.5;8;8.5;10;12;15;20];

%rng(1);%same random seed
%fprintf("indx pr  %i %f\n",indx,pr_vec(indx));

[x(indx),y(indx),z(indx),zz(indx),e(indx),f(indx),g(indx),...
    h(indx),i(indx),j(indx),r(indx),s(indx),uu(indx),vv(indx),pp(indx),ll(indx)] =...
    seqsic(initialK,alldatadecoded,K,...
    pr_vec(2),power_vec,sym_dur_vec,g_vec,max_tx_power,timeslot,N,h_vec);
    z;
    zz;
    i;
    j;
    uu;
    vv;
    pp
    ll
end

save x.mat;
save y.mat;
save z.mat;
save zz.mat;

function [a,b,c,d,e,f,g,h,i,j,r,s,uu,vv,pp,ll] = seqsic(initialK,alldatadecoded,K,priority,power_vec,sym_dur_vec,...
g_vec,max_tx_power,timeslot,N,h_vec)

sim_delay_prop = 0;
sim_delay_conv = 0;
nbiterations=1;

for nbusers = initialK: initialK%number of superimposed data loop
for i = 1:100 %random iterations 
v =1;
%fprintf('K %i\n',K);
while (alldatadecoded == false & K> 1) 

%nsymbols vector of each user: K vec #loop
clear K_vec;
for k = 1:K
    K_vec(k,1) = K-(k-1);
end
%fprintf('K %i\n',K);
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

clear nsym;
clear user_strength;
for k = 1:K
    nsym(k,1) = K-(k-1);
    user_strength(k,1) = k;
end

clear delta_mat;
clear reverse_delta_mat;
%time offsets between users 
%delta_mat: rows -> user index, columns-> symbol index %time offset with
delta_mat = zeros(K,K);
delta_mat(1,:) = zeros(K,1);
delta_mat(2:K,:) = 0.5*rand(K-1,K);%B1,... Bn, C1....,Cn, ....... %Z1,....Zn

reverse_delta_mat(K,:)  = zeros(K,1);
reverse_delta_mat(1:K-1,:) = 0.5*rand(K-1,K);%A1, A2

for j = 1:K%interference vector loop
for k = 1:K
    %interference vec %only from the next neighbor user
    if k ~= desired_id & k == desired_id+1 & desired_id == 1        
        sumsym_dur_vec(desired_id,1) = sum(delta_mat(desired_id+1,:))
        
    elseif k ~= desired_id & k == desired_id+1 & desired_id > 1 & desired_id <K
        sumsym_dur_vec(desired_id,1) = sum(delta_mat(desired_id+1,:))+...
            sum(reverse_delta_mat(desired_id-1,:))
    elseif desired_id==K
        sumsym_dur_vec(desired_id,1) = sum(reverse_delta_mat(desired_id-1,:)); 
       
    end
 desired_id = desired_id+1;
end
end
       
%% optimization problem
pastdelay = 0;
nbiter = 10;
noisepower   = 0.1;

if(K>1)
opt_decision_uk = 0.1*ones(K,1);

proptstart(v)=tic;

n = K;
%% 
cvx_begin quiet
   variable decision_uk(n,1) 
   dual variables lam gan ha kl
   minimize(-decision_uk'*K_vec)
   subject to
      lam : -sum(decision_uk)+ sum(decision_uk.^2)<=0;

      gan: decision_uk'*sumsym_dur_vec-1/(priority+0.001)*priority_max/timeslot <= 0
           
      ha: decision_uk.*((noisepower^2 + interf_vec + power_vec(1:K).*mean(g_vec(1:K,:),2))...
                -power_vec(1:K).*mean(g_vec(1:K,:),2)*(1+1/sinr_th)) <= 0  
      kl: sum(decision_uk)>0
cvx_end

echo off

decision_uk = decision_uk>0.8;

%complexity prop
sic_complextiyprop(v) = sum(decision_uk)^2*log(1/tolerance)*log(1/tolerance);

proptend(v)    = toc(proptstart(v));

%complexity analysis
%proptend(v) = toc(proptstart(v));

random_iterations = 10;
N=10^4;  

userdata_vec = rand(initialK,N)>0.5;          % Generation of data for user1
clear K_vec;
for k = 1:K
    K_vec(k,1) = length(opt_decision_uk)-(k-1);
end

%% ber analysis
clear nsym;
clear user_strength;
for k = 1:K
    nsym(k,1) = K-(k-1);
    user_strength(k,1) = k;
end

clear delta_mat;
clear reverse_delta_mat;
%time offsets between users 
%delta_mat: rows -> user index, columns-> symbol index %time offset with
delta_mat = zeros(K,K);
delta_mat(1,:) = zeros(K,1);
delta_mat(2:K,:) = 0.5*rand(K-1,K);%B1,... Bn, C1....,Cn, ....... %Z1,....Zn

reverse_delta_mat(K,:)  = zeros(K,1);
reverse_delta_mat(1:K-1,:) = 0.5*rand(K-1,K);%A1, A2

mod_order = 4;
timeoff_min = 0.01;
timeoff_max = 0.5;

if K==initialK
    [berfinalconv] = berfunc(power_vec, noisepower, nsym, user_strength,...
    delta_mat,reverse_delta_mat,mod_order,timeoff_min,timeoff_max);
end

[berfinal0] = berfunc(power_vec, noisepower, nsym, user_strength,...
    delta_mat,reverse_delta_mat,mod_order,timeoff_min,timeoff_max);

ber_propuser1(v) = berfinal0(1);
ber_convuser1(v) = berfinalconv(1);
ber_propuserw(v) = berfinal0(K);
ber_convuserw(v) = berfinalconv(K);
ber_propuseri(v) = berfinal0(round(K/2));
ber_convuseri(v) = berfinalconv(round(K/2));
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
    %disp('break');
    nbiterations  = nbiterations+1;
    iterations(v) = nbiterations;
else
    nbiterations  = nbiterations+1;
    iterations(v) = nbiterations;
    %fprintf('nbiterations %i\n',nbiterations);
    decision_uk(1) = 1;%make sure decision_uk is non zero
    %break;
end%end if 

end%end if 
K = K-sum(decision_uk);%update K

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
end %end while

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

avgberconvuser1(i) = mean(ber_convuser1);
avgberuser1(i) = mean(ber_propuser1);

avgberweakprop = mean(ber_propuserw);
avgberweakconv = mean(ber_convuserw);

avgberinterprop = mean(ber_propuseri);
avgberinterconv = mean(ber_convuseri);

end
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

r = mean(avgberconvuser1); 
s = mean(avgberuser1); 

uu = mean(avgberweakconv);
vv = mean(avgberweakprop);

pp = mean(avgberinterconv); 
ll = mean(avgberinterprop); 

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
%ber(i) = abs(mean(mean(est_sym - userdata_vec(:,1:3),2)));
ber = 0;
propend(i) = toc(proptstart(i));
end
sim_delay  = mean(propend);
ber_mean = mean(ber);
end

function [convergedukfin,nbiterationslam,lam,nbiterationsuk,decision_uk] =...
    grad_descent_uklam(grad_lam,...
    lam,learn_rate,n_iter,tolerance,K_vec,decision_uk,K,sym_dur_vec, energyth)
    if K>5
        startlam = 1.15;
        mew = 1.15;
    else 
        startlam = 0.9;
        mew = 0.9;
    end
    
    convergeduk = false;    
    convergedlam = false;
    convergedmew = false;
    nbiterationslam = 1;
    nbiterationsuk  = 1;
    
    while(convergedlam==false & convergedmew==false)
        grad_uk = -K_vec-lam...
                            + 2*lam'*decision_uk;
                                        
        diffuk  = -learn_rate*(grad_uk);       
        if (abs(diffuk)<= tolerance)
            convergeduk = true;
            nbiterationsuk = nbiterationsuk+1;
            
            while(convergeduk == true)
                grad_lam = -sum(decision_uk)...
                + sum(decision_uk.^2);
                %grad_mew = (decision_uk'*sym_dur_vec) - energyth ;
                diff = -learn_rate*grad_lam;
                
                %diffmew = -learn_rate*grad_mew;
                
                if (abs(diff)<= tolerance)
                    converged_lam = lam;
                    nbiterationslam = nbiterationslam+1;
                    convergedlam = true;
                    convergeduk = false;   
                    convergedukfin = true;
                    decision_uk =decision_uk>0.8;
                else
                    converged_lam = 0;
                    nbiterationslam = nbiterationslam+1;
                    lam = lam + diff;                   
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

function [berfinal] = berfunc(power_vec, noise, nsym, user_strength,...
    delta_mat,reverse_delta_mat,mod_order,timeoff_min,timeoff_max)

for i = 1: length(user_strength)
for j = 1: nsym(i)
    
if user_strength(i) == 1 & j == 1%A1
    %interf by B1, s+1
    delta_i = delta_mat(user_strength(i+1),j);%known
    p_d     = power_vec(i); %desired power
    p_iw    = power_vec(i+1);%interferes power 
    %disp('yea')
    fun = @(delta_i) (qfunc(sqrt(3*p_d./(2.*(mod_order-1).*...
    (delta_i.*p_iw/2+noise))))).^2;
    q   = integral(fun,timeoff_min,timeoff_max);
    p_err_sym1 = (1/(timeoff_max -timeoff_min))*q*delta_i;
    p_bita1    = p_err_sym1/log(mod_order);
    ber_vec(i,1) = p_bita1;
    
elseif (user_strength(i) == 1 & j > 1)%A2.... An
    %disp('no')
    %interf->B1 and B2 %s-1 and s+1
    delta_i = [(1-delta_mat(user_strength(i+1),j-1)); ...
        delta_mat(user_strength(i+1),j)];
    p_d     = power_vec(i); %desired power
    p_iw     = power_vec(i+1);%interferes power
    power_v  = [p_iw/2;p_iw/2];
    fun = @(delta_i) (qfunc(sqrt(3*p_d./(2.*(mod_order-1).*...
        (sum(delta_i.*power_v)+noise))))).^2;
    q   = integral(fun,timeoff_min,timeoff_max);
    p_err_sym2 = (1/(timeoff_max -timeoff_min))*q*sum(delta_i);
    p_bita2 = p_err_sym2/log(mod_order); 
    ber_vec(i,j) = p_bita2;
    
elseif (user_strength(i) > 1 & j == 1 & i~=length(user_strength))%B1
    %inter -> A1, A2 and C1
    %disp('here0')
    delta_i = [(reverse_delta_mat(user_strength(i-1),j));...
        (1-reverse_delta_mat(user_strength(i-1),j+1)); ...
        delta_mat(user_strength(i+1),j);];
    detected_vec = [(6/(mod_order-1));(6/(mod_order-1));1;];
    p_d     = power_vec(i); %desired power
    p_is    = power_vec(i-1);%interferes power
    p_iw    = power_vec(i+1);%interferes power
    power_v  = [p_is/2;p_is/2;p_iw/2];
    %include the delta i into the func expression???????
    fun = @(delta_i) (qfunc(sqrt(3*p_d./(2.*(mod_order-1).*...
        (sum(delta_i.*power_v)+noise))))).^2;
    q   = integral(fun,timeoff_min,timeoff_max);
    p_interb1 = (1/(timeoff_max -timeoff_min))*q*sum(delta_i);
    p_err_sym2 = p_interb1*(ber_vec(i-1,j)*ber_vec(i-1,j+1)+...
        (1-ber_vec(i-1,j))*ber_vec(i-1,j+1)+(ber_vec(i-1,j))*(1-ber_vec(i-1,j+1))...
        +(1-ber_vec(i-1,j))*(1-ber_vec(i-1,j+1)));
    p_bita2 = p_err_sym2/log(mod_order); 
    ber_vec(i,j) = p_bita2;
    
elseif (user_strength(i) > 1 & j > 1 & i~=length(user_strength))%B2.....Bn & not last user 
    %disp('here1 ')
    %inter -> A2, A3 and C1, C2
    nbinterf = 4;
    delta_i = zeros(nbinterf,1);
    for h = 1: nbinterf
        if h == 1
            delta_i(h) = (reverse_delta_mat(user_strength(i-1),j));
        elseif h == 2
            delta_i(h) = 1-reverse_delta_mat(user_strength(i-1),j+1);
        elseif h == 3
            delta_i(h) = (1-delta_mat(user_strength(i+1),j-1));
        else
            delta_i(h) = delta_mat(user_strength(i+1),j);
        end
    end
    detected_vec = [(6/(mod_order-1));(6/(mod_order-1));1;1;];
    p_d     = power_vec(i); %desired power
    p_is    = power_vec(i-1);%interferes power
    p_iw    = power_vec(i+1);%interferes power
    power_v  = [p_is/2;p_is/2;p_iw/2;p_iw/2];
    fun = @(delta_i) (qfunc(sqrt(3*p_d./(2.*(mod_order-1).*...
        (sum(detected_vec.*delta_i.*power_v) +noise))))).^2;
    q   = integral(fun,timeoff_min,timeoff_max);
    p_interb2 = (1/(timeoff_max - timeoff_min))*q*sum(delta_i);
    p_err_sym2 = p_interb2*(ber_vec(i-1,j)*ber_vec(i-1,j+1)+...
        (1-ber_vec(i-1,j))*ber_vec(i-1,j+1)+(ber_vec(i-1,j))*...
        (1-ber_vec(i-1,j+1))...
        +(1-ber_vec(i-1,j))*(1-ber_vec(i-1,j+1)));
    p_bita3 = p_err_sym2/log(mod_order);
    ber_vec(i,j) = p_bita3;
    
elseif (user_strength(i) > 1 & j >= 1 & i==length(user_strength))
    %disp('here2 ')
    %interf-> B1 and B2
    delta_i =[(reverse_delta_mat(user_strength(i-1),j)); ...
        1-reverse_delta_mat(user_strength(i-1),j+1)];
    detected_vec = [(6/(mod_order-1));(6/(mod_order-1))];
    p_d     = power_vec(i); %desired power
    p_is    = power_vec(i-1);%interferes power
    power_v  = [p_is/2;p_is/2;];
    fun = @(delta_i) (qfunc(sqrt(3*p_d./(2.*(mod_order-1).*...
        (sum(detected_vec.*delta_i.*power_v)+noise))))).^2;
    q   = integral(fun,timeoff_min,timeoff_max);
    p_interb3 = (1/(timeoff_max -timeoff_min))*q*sum(delta_i);
    p_err_sym3 = p_interb3*(ber_vec(i-1,j)*ber_vec(i-1,j+1)+...
        (1-ber_vec(i-1,j))*ber_vec(i-1,j+1)+(ber_vec(i-1,j))*...
        (1-ber_vec(i-1,j+1))...
        +(1-ber_vec(i-1,j))*(1-ber_vec(i-1,j+1)));
    p_bita4 = p_err_sym3/log(mod_order);
    ber_vec(i,j) = p_bita4;
else
    %disp('oops')
end
end
end
berfinal = sum(ber_vec,2);
end