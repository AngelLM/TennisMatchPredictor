function p = predict(theta, X)
%PREDICT Predict whether the label is 0 or 1 using learned logistic regression parameters theta

m = size(X, 1); % Number of training examples

p = zeros(m, 1);

z = theta'*X';                % We use X' because X is the array[mₓ1] composed by (Xᵐ)ᵀ
h = sigmoid(z);               % h dimension is (1ₓm)

p = h'>=0.5;                    % We check if h' is >=0.5. This code will asign to p a matrix with the dimension of h' (mₓ1). Filled with 1's if the value is >=0.5 and 0's if <0.5.

end
