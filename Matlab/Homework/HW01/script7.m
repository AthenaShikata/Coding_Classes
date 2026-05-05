format long
N = 1;
myPi = myApproximationPI(N);
piDif = abs(myPi - pi);

fprintf("\nMy approximation of pi is: %.20f\n",myPi)
fprintf("Matlab's stored approximation of pi is: %.20f\n",pi)
fprintf("The difference between my approximation and Matlab's is: %.20f or %.5e\n\n",piDif,piDif)