% 1-D list
my_list = {1, 2, 3, 'apple', 'banana', {4, 5, 6}};

disp(my_list{1});
disp(my_list{4});
disp(my_list{6});

% 2-D list
two_d_list = {
    [1, 2, 3];
    [4, 5, 6];
    [7, 8, 9]
};

disp(two_d_list{1});
disp(two_d_list{1}(1));
disp(two_d_list{2}(3));

% Uneven 2-D list
two_d_list = {
    [1, 2];
    [4, 5, 6];
    [7, 8, 9, 1, 3]
};

% Modifying a List
my_list{2} = 'orange';
disp(my_list);

my_list{end+1} = 'grapes';
disp(my_list);

disp(my_list);
my_list = [my_list(1), {'apple'}, my_list(2:end)];
disp(my_list);

% Append vs Extend
my_list = {'apple', 'banana'};
my_list{end+1} = [1, 2, 3];
disp(my_list);

my_list = {'apple', 'banana'};
my_list = [my_list, {1, 2, 3}];
disp(my_list);

% Remove elements
my_list = {'banana', 'banana', 'apple', 'orange', 'green', 'red'};
my_list(strcmp(my_list, 'banana')) = [];
disp(my_list);

disp(my_list);
elt = my_list{end};
my_list(end) = [];
disp(elt);
disp(my_list);

disp(my_list);
elt = my_list{2};
my_list(2) = [];
disp(elt);
disp(my_list);

disp(my_list);
my_list = {};
disp(my_list);
