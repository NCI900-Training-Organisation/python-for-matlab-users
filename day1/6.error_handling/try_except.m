try
    % Code that may raise an error
    result = 10 / 0;
catch ME
    % Code to handle the error
    disp('An error occurred:');
    disp(ME.message);
end
disp('Execution completed.');
