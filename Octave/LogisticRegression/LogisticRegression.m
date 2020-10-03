% Load the dataset
data = csvread('../../Database/addapteddatabase.csv');

% Discard the first row (headers)
data = data(2:end, :);

% Get number of samples
totalSamples =  length(data);

% Create a random index vector to split the dataset into Training Set (60%), Cross Validation Set (20%) and Test Set (20%)
rowList = randperm(totalSamples);

dataTrain = data(rowList(1:totalSamples*0.6), :);
dataVal = data(rowList(totalSamples*0.6+1:totalSamples*0.8), :);
dataTest = data(rowList(totalSamples*0.8+1:end), :);

% Get the features from the dataset
X = dataTrain(:, [1:16]);
Xval = dataVal(:, [1:16]);
Xtest = dataTest(:, [1:16]);

% Get the labels from the dataset
y = dataTrain(:, 17);
yval = dataVal(:, 17);
ytest = dataTest(:, 17);

% Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1);

% Set regularization parameter lambda
lambda = 0;

% Set Options
options = optimset('GradObj', 'on', 'MaxIter', 400);

% Optimize
iter=100;
opt_theta = zeros(size(X, 2), iter);
J = zeros(iter);
errorval = zeros(iter,1);
lambdas = zeros(iter,1);
lambda = 0.000001;
for i = 1:iter
    [opt_theta(:,i), J(i), exit_flag] = fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);
    pval = predict(opt_theta(:,i), Xval);
    errorval(i) = sum((pval-yval).^2)/(2*length(yval));
    lambdas(i) = lambda;
    lambda = lambda * 2;
endfor

[minval, iminval] = min(errorval);
theta = opt_theta(:,iminval);

% Compute Accuracy on our Test Set
ptest = predict(theta, Xtest);
fprintf('Test Accuracy: %f\n', mean(double(ptest == ytest)) * 100);
