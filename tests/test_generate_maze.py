from app.models.maze.generate_maze import InputValidation


def test_input_validation_to_be_invalid_size():
    size_31 = InputValidation().validate(31, "RecursiveBacktracking")
    assert size_31 is False
    size_2 = InputValidation().validate(2, "RecursiveBacktracking")
    assert size_2 is False
    size_negativ3 = InputValidation().validate(-3, "RecursiveBacktracking")
    assert size_negativ3 is False


def test_input_validation_to_be_invalid_type():
    type_recursive = InputValidation().validate(15, "Recursive")
    assert type_recursive is False
    type_backtracking = InputValidation().validate(15, "Backtracking")
    assert type_backtracking is False
    type_empty = InputValidation().validate(15, "")
    assert type_empty is False


def test_input_validation_to_be_valid_type():
    type_recursive_backtracking = InputValidation().validate(15, "RecursiveBacktracking")
    assert type_recursive_backtracking is True
    type_sidewinder = InputValidation().validate(15, "Sidewinder")
    assert type_sidewinder is True
