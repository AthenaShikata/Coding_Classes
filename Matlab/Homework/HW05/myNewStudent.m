function [newStudent] = myNewStudent(name, id, grades)
    % Create a struct array with fields: name, id, and grades
    newStudent.name = name;
    newStudent.id = id;
    newStudent.grades = grades;
end