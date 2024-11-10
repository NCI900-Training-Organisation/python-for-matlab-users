
my_tuple = {1, 'red', 3, 'green', 5};
disp('Original tuple:');
disp(my_tuple);

disp(my_tuple{2});
disp(my_tuple{5});
disp(my_tuple{6});

index_of_3 = find(cell2mat(my_tuple) == 3);
disp('Index of 3 in the tuple:');
disp(index_of_3);

sliced_tuple = my_tuple(2:4);
disp(sliced_tuple);

another_tuple = {6, 7, 8};
concatenated_tuple = [my_tuple, another_tuple];
disp('Concatenated tuple:');
disp(concatenated_tuple);

repeated_tuple = repmat(my_tuple, 1, 2);
disp('Repeated tuple:');
disp(repeated_tuple);

exists = ismember(3, cell2mat(my_tuple));
disp('Does 3 exist in the tuple?');
disp(exists);

not_exists = ismember(10, cell2mat(my_tuple));
disp('Does 10 exist in the tuple?');
disp(not_exists);

tuple_length = numel(my_tuple);
disp('Length of the tuple:');
disp(tuple_length);

count_of_2 = sum(cell2mat(my_tuple) == 2);
disp('Count of 2 in the tuple:');
disp(count_of_2);

nested_tuple = {my_tuple, another_tuple};
disp('Nested tuple:');
disp(nested_tuple);

disp(nested_tuple{1});
disp(nested_tuple{2});
