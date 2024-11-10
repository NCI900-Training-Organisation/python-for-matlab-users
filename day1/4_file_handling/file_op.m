% Create and write to a file
fileID = fopen('example.txt', 'w');  % Open file in write mode
if fileID == -1
    error('Failed to open file for writing.');
end

% Write data to the file
fprintf(fileID, 'Hello, this is a simple file handling example in MATLAB.\n');
fprintf(fileID, 'It demonstrates writing, reading, and manipulating the file pointer.\n');
fclose(fileID);  % Close the file after writing

% Reading from the file
fileID = fopen('example.txt', 'r');  % Open file in read mode
if fileID == -1
    error('Failed to open file for reading.');
end

% Read the entire content of the file
fileContent = fread(fileID, '*char')';  % Read the file as characters
disp('File content after read:');
disp(fileContent);

% Use ftell to get the current position in the file
position = ftell(fileID);
disp(['Current file pointer position after reading: ', num2str(position)]);

% Use fseek to move the file pointer
% Move to the start of the file
fseek(fileID, 0, 'bof');
disp('File pointer moved to the beginning.');

% Read first 10 characters
first10Chars = fread(fileID, 10, '*char')';
disp('First 10 characters:');
disp(first10Chars);

% Use ftell to get the current position in the file after reading
position = ftell(fileID);
disp(['Current file pointer position: ', num2str(position)]);

% Close the file after reading
fclose(fileID);
