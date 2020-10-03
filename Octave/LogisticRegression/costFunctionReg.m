function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization

% Initialize some useful values
m = length(y); % number of training examples

J = 0;
grad = zeros(size(theta));

%                                            m                                              n
% The regularized cost function: J(θ)= (1/m) ∑[-yᶦlog(hθ(xᶦ))-(1-yᶦ)log(1-hθ(xᶦ))] + (λ/2m) ∑θⱼ²
%                                           i=1                                            j=1

z = theta'*X';
h = sigmoid(z);

J=(1/m)*sum(-y'.*log(h)-(1-y').*log(1-h))+(lambda/(2*m))*sum(theta(2:end).^2);    % theta(2:end).^ will return an array of (n-1ₓ1) dimension with the values of θ (except for θ₀)


%                                       m
% Gradient equation for j= 0 is : (1/m) ∑[(hθ(xᶦ)-yᶦ)Xⱼᶦ]   which is the same of not regularized cost function
%                                      i=1

%                                      m
% Gradient equation for j>=1 is: (1/m) ∑[(hθ(xᶦ)-yᶦ)Xⱼᶦ] + (λ/m)θⱼ
%                                     i=1


% First we compute the gradiend as if every j is regularized (including j=0)
grad = (1/m)*sum((h-y').*X',2)+(lambda/m)*theta;

% Then, as j=0 should not be regularized, we will replace the first term on grad array with the correct gradient for j=0
grad(1) = (1/m)*sum((h-y').*X',2)(1);

end
