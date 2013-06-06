experiment = importdata('radioactivedecay.dat')
t = experiment.data(:,1);
N = experiment.data(:,2);
figure(42)
plot(t,N,'.b')
hold off
%put hold on to plot all at once
%%
% function to fit
func = @(a,b,c,x) -sqrt(a^2-(x-b).^2)+c;
%I just gotta find good guesses then it should work just dandy
guesss = func(6,0,6,x);
plot(x,guesss,'r:')
%%
%un comment out once guesses are found
% fit the data
%fittedmodel = fit(x',y',func,'StartPoint',[15,0,15])
%plot result
%plot(fittedmodel,'r-')
%xlabel('t')
%ylabel('N')
%axis equal