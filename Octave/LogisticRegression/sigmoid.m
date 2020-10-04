function g = sigmoid(z)
%SIGMOID Compute sigmoid function

g = zeros(size(z));     % We create the "g" matrix, filled with "0", which has the same size as the "z" matrix.

g = 1./(1+(e.^(z*-1)));

end
