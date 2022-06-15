echo on

n = 10;
K = n
priority =0.5;
priority_max = 200;
timeslot =1;
sumsym_dur_vec =[0.5;0.3;0.2;0.4;0.5;0.3;0.2;0.4;0.5;0.4];
noisepower =0.1;
power_vec = [1;0.9;0.8;0.7;0.6;0.5;0.4;0.3;0.2;0.1]
interf_vec = [0.5;0.5;0.3;0.2;0.1;0.5;0.4;0.3;0.5;0.4]
K_vec = [10;9;8;7;6;5;4;3;2;1];

cvx_begin
   variable decision_uk(n,1) 
   dual variables lam mu v
   minimize(-decision_uk'*K_vec)
   subject to
      lam : -sum(decision_uk)+ sum(decision_uk.^2)<=0;
      %mu : sum(decision_uk) > 0;
      mu: decision_uk'*sumsym_dur_vec- ...
               1/(priority+0.001)*priority_max/timeslot <=0
      v:  decision_uk.*((noisepower^2 + interf_vec + power_vec(1:K).*mean(g_vec(1:K,:),2))...
                -power_vec(1:K).*mean(g_vec(1:K,:),2)*(1+1/sinr_th) ) <= 0   
cvx_end

echo off

decision_uk>0.8
