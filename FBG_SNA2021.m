% This code is written by Abdullah Al-Azzawi on 06.Oct.2023

% We have made the source codes for the simulations conducted in this study available 
% on our GitHub repository: {https://github.com/abd-alaz/spiral-sensors}. Interested 
% readers can access and download the codes for a closer examination of the implementations
% and methods employed. The codes are open-source and provided under the GNU General 
% Public License v3.0, allowing for academic and non-commercial use.

% This code is to compare between our theoretical spiral sensor model and
% the experimental results from the following paper:

% [1] Khan, Fouzia, David Barrera, Salvador Sales, and Sarthak Misra. "Curvature, 
% twist and pose measurements using fiber Bragg gratings in multi-core 
% fiber: A comparative study between helical and straight core fibers." 
% Sensors and Actuators A: Physical 317 (2021): 112442.


% The authors conducted experimental work to test two sets of sensors, straight
% and helical optical fibres. Each set has three fibres with 120deg apart.
% Each fibre contains multiple FBG sensors which is irrelevant to us since
% we are interested in the strain of the whole fibres.

% In total, we do have 6 sensors (3 straight, and 3 helical)





clc;clear;


% set some initial values

% helical sample length = 175mm
% straight sample length = 115.5mm
% assume both samples length is 1 mtr = 1000mm (i.e. per unit length)

% Straight FBG sensor:
%   radius  = 35 micrometer = 0.035mm

% Helical FBG sensor:
%   radius  = 35 micrometer = 0.035mm
%   turns   = 50 turns / mtr

% define our model parameters
R = 0.035;         	% tube radius in mm
psi = 0;        	% no twisting
ho_st = 115.5;      % centreline length in mm, straight sample
ho_hl = 175;        % centreline length in mm, helical sample
k_ini = 0;			% initial position is straight (no bending)
tspan = [0 1];  	% integration limits
Lo = 0;         	% initial length value for integration, t = 0 > L = 0
n = 50;				% helix turns per mtr (or per 1000 mm)
sen_ang = deg2rad(120);     % angle between sensors



% load readings as acquired from figures

% curv:         curvature values as per bending test
% twst:         tip rotation and twist values as per twist test
% fbg_hl:       reconstructed curvature measurements for helical FBG fibres in bending
% fbg_st:       reconstructed curvature measurements for straight FBG fibres in bending


% description of data:
% ---------------------
%
% curv: has one column represents the curvature at each bending test.
%
% twst: has two columns, first column represents the rotation angle (in rad)
%       at the tip of the sample (length = 0.175 m), and the second column 
%       is the adjusted twist angle per unit length (in rad/m) for ACW
%       which are positive. The same column is used for CW but in negative.
%
% each of fbg_hl and fbg_st has 3 columns:
%   first column:   lower bound measurements.
%   second column:  mean values of measurements.
%   third column:   upper bound measurements.
%
% No useful data for straight sensors under twisting as the authors 
% acknowledge a physical limitation in the test set-up




load FBG_SNA2021_data.mat

cr = length(curv);				% number of bending tests (number of curvatures)


% sensors are numbered in a CW order, so the angle is negative 
% define 3 sensors for the straight FBG fibres
vs_st = [0;-sen_ang;-2*sen_ang];        % location of straight sen 1,2,3 as per ([1], fig2)
dv_st = [0;0;0];                        % angle difference of each sensor
                                        % sensors are straight, so dv=0



% define 3 sensor for the helical FBG fibres
hang = 2*pi*n*ho_hl/1000;		        % total helix angle in rad
vs_hl = [0;-sen_ang;-2*sen_ang];        % location of helical sen 1,2,3 as per ([1], fig2)
dv_hl = [hang;hang;hang];               % angle difference of each sensor
                                        % sensors are straight, so dv=0


% no rotation at initial position
phi = 0;


% define two vectors for initial lengths of straight and helical FBG fibres
% total is 6 vectors
Ls_st_ini = zeros(3,1);
Ls_hl_ini = zeros(3,1);

% calculate sensors length at initial position 
% no bending, rotation, or twisting
% for straight FBG sensor
for i=1:3
    % straight
    vsi = vs_st(i); dvi = dv_st(i); ho = ho_st;
    [~,L] = ode45(@(t,L) Lenfun(R,dvi,psi,ho,k_ini,vsi,phi,t),tspan,Lo);
    Ls_st_ini(i) = L(end);
    
    % helical
    vsi = vs_hl(i); dvi = dv_hl(i); ho = ho_hl;
    [~,L] = ode45(@(t,L) Lenfun(R,dvi,psi,ho,k_ini,vsi,phi,t),tspan,Lo);
    Ls_hl_ini(i) = L(end);

end






% -------------------------------------------------
% -------------------------------------------------


% Bending test






% define empty vectors for the lengths at each curvature
Ls_st = zeros(3,cr); 
Ls_hl = zeros(3,cr); 


% rotation angle is constant as per [1]
% technically, phi value will not affect the results since ref[1],eq7 is
% calculating the magnitude of the curvature vector v=[v1;v2]
% so, any phi value should give similar results
% when phi = 0, sen2 and sen3 will produce similar results
phi = 0;        % in rad


% solve the differential equation to calculate length vectors
for j=1:cr          % loop for curvatures 

    k = curv(j);  
    for i=1:3       % loop for 3 sensors per set 

        % straight 
        vsi = vs_st(i); dvi = dv_st(i); ho = ho_st;
        [~,L] = ode45(@(t,L) Lenfun(R,dvi,psi,ho,k,vsi,phi,t),tspan,Lo);
        Ls_st(i,j) = L(end);
    
	    % helical
        vsi = vs_hl(i); dvi = dv_hl(i); ho = ho_hl;
        [~,L] = ode45(@(t,L) Lenfun(R,dvi,psi,ho,k,vsi,phi,t),tspan,Lo);
        Ls_hl(i,j) = L(end);
    end
end


% calculate strain
% Matlab will do the correct math between arrays (Ls_st,hl) and vectors (Ls_st,hl_ini)
st_st = (Ls_st - Ls_st_ini)./Ls_st_ini;          % straight FBG
st_hl = (Ls_hl - Ls_hl_ini)./Ls_hl_ini;          % helical FBG



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% use Fouzoia's equations to calculate results of fig5 @ ref[1]
% since there are no actual experimental measurements, I will use the strain values from
% our model to calculate curvature and twist as per ref[1] equations (equations 7 and 8). 
% The FBG gauge factor S is eliminated while calculating curvature vector in eq7
% S is a scalar value representing the FBG gauge factor

% assume C = S * CC ----> pinv(C) = pinv(S*CC) = Pinv(CC) / S 
% assume Z = (1/S) * zeta = (1/s) (mi - m4) - e_t = e_i - e_t ,  since m4 = 0 as it is fpr the centreline
% Now, in eq7, v = pinv(C) * zeta ---> v = pinv(CC) * Z

% The CC matrix is for 3 FBG fibres with 120deg apart,
CC = [-1,0;0.5,0.866;0.5,-0.866].*R;	% full C matrix without S

% zeta vector is the actual measurements of the FBG sensors,
% however, I don't have experimental measurements 
% instead, use Z instead of zeta as explained above
% so, Z_st for straight, and Z_hl for helical strain readings (not wavelength)

% calculate torsional strain as per (ref[1], eq 6)
st_tor_st = mean(st_st);        % mean of each column, straight
st_tor_hl = mean(st_hl);        % mean of each column, helical

% calculate Z array
% MATLAB will subtract the column vector (st_tor_st,hl) from each column in
% the array (st_st,hl). No need to do a separate loop for that.
Z_st = st_st - st_tor_st;		% strain readings for straight sensor
Z_hl = st_hl - st_tor_hl;		% strain readings for helical sensor


% initialise curve results vectors (defined as v = [v1;v2] in ref[1], eq7)
curv_vst = zeros(2,cr);     % each column is a vector [v1;v2]
curv_vhl = zeros(2,cr);     % each column is a vector [v1;v2]

kappa_st = zeros(cr,1);     % total curvature kappa as per ref[1],eq 7
kappa_hl = zeros(cr,1);     % total curvature kappa as per ref[1],eq 7

for j=1:cr
	curv_vst(:,j) = pinv(CC) *  Z_st(:,j);		% curvature results for straight
    curv_vhl(:,j) = pinv(CC) *  Z_st(:,j);		% curvature results for straight

    kappa_st(j) = norm(curv_vst(:,j));          % magnitude of curvature vector
    kappa_hl(j) = norm(curv_vhl(:,j));          % magnitude of curvature vector
end


% Compare theoretical vs experimental
% results of kappa_st,hl should be similar to curv values if there is no twist




% plot results using a grid of 2x3 subplots (2 rows x 3 columns)
% top row is for exp vs theo results
% lower row is for error percentage 




% Create figure
fig1 = figure; 
fig1.Position = [250 250 1000 1000];     % set the location, and size (1000x1000 pixels)
                                        % this will make it suitable for publishing



% subplot for straight sensors at bending
% subplot location: first row, and first column
ax1 = subplot(2,2,1,'Parent',fig1); 
hold(ax1,'on');

% theoritical results
plot(1:cr,kappa_st,'DisplayName','Theo','LineWidth',2);

% experimental results (ref)
fbg_st_mean = fbg_st(:,2);
fbgerr_st_neg = fbg_st_mean - fbg_st(:,1);
fbgerr_st_pos = fbg_st(:,3) - fbg_st_mean;

p_bst_exp = errorbar(1:7,fbg_st_mean,fbgerr_st_neg,fbgerr_st_pos,'o');
set(p_bst_exp,'DisplayName','Exp(ref)','LineWidth',2,'MarkerSize',10, ...
    'LineStyle','none','Color',[0.467 0.675 0.188]);

% theoritical results (ref)
plot(1:cr,curv,'x','DisplayName','Theo(ref)','LineWidth',2, ...
    'MarkerSize',15,'Color',[1 0 0],'LineStyle','none');

% Set properties
ylabel(ax1,'Curvature (1/m)');
xlabel(ax1,'Slot Number');
title(ax1,'Straight');
xlim(ax1,[0.5 7.5]);
ylim(ax1,[0 7]);
box(ax1,'on');
set(ax1,'FontSize',14,'FontWeight','bold','XGrid','on','YGrid','on');
set(ax1,'XTick',[1 2 3 4 5 6 7]);
lgnd1 = legend(ax1,'show');
set(lgnd1,'Location','southeast','FontSize',12);




% subplot for helical (or spiral) sensors at bending
% subplot location: first row, and second column
ax2 = subplot(2,2,2,'Parent',fig1); 
hold(ax2,'on');

% theoretical results
plot(1:cr,kappa_st,'DisplayName','Theo','LineWidth',2);

% experimental results (ref)
fbg_hl_mean = fbg_hl(:,2);
fbgerr_hl_neg = fbg_hl_mean - fbg_hl(:,1);
fbgerr_hl_pos = fbg_hl(:,3) - fbg_hl_mean;

p_bhl_exp = errorbar(1:7,fbg_hl_mean,fbgerr_hl_neg,fbgerr_hl_pos,'o');
set(p_bhl_exp,'DisplayName','Exp(ref)','LineWidth',2,'MarkerSize',10, ...
    'LineStyle','none','Color',[0.467 0.675 0.188]);

% theoretical results (ref)
plot(1:cr,curv,'x','DisplayName','Theo(ref)','LineWidth',2, ...
    'MarkerSize',15,'Color',[1 0 0],'LineStyle','none');


% Set properties
ylabel(ax2,'Curvature (1/m)');
xlabel(ax2,'Slot Number');
title(ax2,'Spiral');
xlim(ax2,[0.5 7.5]);
ylim(ax2,[0 7]);
box(ax2,'on');
set(ax2,'FontSize',14,'FontWeight','bold','XGrid','on','YGrid','on');
set(ax2,'XTick',[1 2 3 4 5 6 7]);
lgnd2 = legend(ax2,'show');
set(lgnd2,'Location','southeast','FontSize',12);







%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% error values are between our theoretical model and experimental results,
% using our model as the base

% error % = 100 * (our model - exp) / our model

% straight sensors at bending test
err_st = 100 * (kappa_st - fbg_st_mean) ./ kappa_st;    % vs exp(ref)
err_stt = 100 * (kappa_st - curv) ./ kappa_st;          % vs theo(ref)

% spiral (helical) sensors at bending test
err_hl = 100 * (kappa_hl - fbg_hl_mean) ./ kappa_hl;    % vs exp(ref)
err_hlt = 100 * (kappa_hl - curv) ./ kappa_hl;          % vs theo(ref)



% subplot for error results of straight sensors at bending tests
% subplot location: second row, and first column
ax3 = subplot(2,2,3,'Parent',fig1); 
hold(ax3,'on');

plot(err_st,'-o','DisplayName','Theo vs Exp(ref)','LineWidth',2)
plot(err_stt,'-x','DisplayName','Theo vs Theo(ref)','LineWidth',2,'MarkerSize',15)

% Set properties
ylabel(ax3,'Error (%)');
xlabel(ax3,'Slot Number');
xlim(ax3,[0.5 7.5]); ylim(ax3,[-4 4]);
box(ax3,'on');
set(ax3,'FontSize',14,'FontWeight','bold','XGrid','on','YGrid','on');
set(ax3,'XTick',[1 2 3 4 5 6 7]);
lgnd3 = legend(ax3,'show');
set(lgnd3,'Location','southeast','FontSize',12);



% subplot for strain results of spiral sensors at bending test
% subplot location: second row, and second column
ax4 = subplot(2,2,4,'Parent',fig1); 
hold(ax4,'on');

plot(err_hl,'-o','DisplayName','Theo vs Exp(ref)','LineWidth',2)
plot(err_hlt,'-x','DisplayName','Theo vs Theo(ref)','LineWidth',2,'MarkerSize',15)

% Set properties
ylabel(ax4,'Error (%)');
xlabel(ax4,'Slot Number');
xlim(ax4,[0.5 7.5]); ylim(ax4,[-4 4]);
box(ax4,'on');
set(ax4,'FontSize',14,'FontWeight','bold','XGrid','on','YGrid','on');
set(ax4,'XTick',[1 2 3 4 5 6 7]);
lgnd4 = legend(ax4,'show');
set(lgnd4,'Location','southeast','FontSize',12);








% theoretical strain results (if anyone is interested)
% sen1_hl = plot(1:cr,st_hl(1,:),'DisplayName','Sen1','LineWidth',2);
% sen2_hl = plot(1:cr,st_hl(2,:),'DisplayName','Sen2','LineWidth',2);
% sen3_hl = plot(1:cr,st_hl(3,:),'DisplayName','Sen3','LineWidth',2);
% sen1_st = plot(1:cr,st_st(1,:),'DisplayName','Sen1','LineWidth',2);
% sen2_st = plot(1:cr,st_st(2,:),'DisplayName','Sen2','LineWidth',2);
% sen3_st = plot(1:cr,st_st(3,:),'DisplayName','Sen3','LineWidth',2);










return





% The length differential function
% notations are as per my draft paper
% the integration of this function will give the length along the sensor
% path until reaching t = 1 which will give the total length of the sensor


function dlen = Lenfun(R,dv,psi,h,k,vsi,phi,t)
    dlen = sqrt(R^2*(dv+psi).^2 + h^2*(1-R*k*cos(vsi+t*(dv+psi)-phi))^2);
end















