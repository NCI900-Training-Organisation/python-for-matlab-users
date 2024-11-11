my_dict = struct('name', 'Alice', 'age', 30, 'city', 'New York', 'hobbies', {'reading', 'travelling', 'swimming'});
disp(my_dict)

disp(my_dict.name)
disp(my_dict.hobbies)
disp(my_dict.age)

my_dict.occupation = 'Engineer';
disp(my_dict)

my_dict.age = 31;
disp(my_dict)

my_dict = rmfield(my_dict, 'city');
disp(my_dict)

age = my_dict.age;
my_dict = rmfield(my_dict, 'age');
disp(my_dict)
disp(age)

exists = isfield(my_dict, 'name');
disp(exists)

not_exists = isfield(my_dict, 'city');
disp(not_exists)

keys = fieldnames(my_dict);
disp(keys)

values = struct2cell(my_dict);
disp(values)

items = [keys, values];
disp(items)

my_dict = struct('name', 'Alice', 'age', 30, 'city', 'New York', 'hobbies', {'reading', 'travelling', 'swimming'});

another_dict = struct('email', 'alice@example.com', 'age', 31);
my_dict = updateStruct(my_dict, another_dict);

disp(my_dict)

function updatedStruct = updateStruct(struct1, struct2)
    fields = fieldnames(struct2);
    for i = 1:numel(fields)
        struct1.(fields{i}) = struct2.(fields{i});
    end
    updatedStruct = struct1;
end
