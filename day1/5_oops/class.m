classdef Car
    % Define properties (attributes)
    properties
        make
        model
        year
    end
    
    % Define methods (functions)
    methods
        function obj = Car(make, model, year)
            % Constructor method to initialize object properties
            obj.make = make;
            obj.model = model;
            obj.year = year;
        end
        
        function displayInfo(obj)
            % Display method to print object info
            fprintf('%d %s %s\n', obj.year, obj.make, obj.model);
        end
        
        function obj = setMake(obj, make)
            % Setter method to update the make
            obj.make = make;
        end
        
        function obj = setModel(obj, model)
            % Setter method to update the model
            obj.model = model;
        end
    end
end
