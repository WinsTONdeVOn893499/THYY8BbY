# 代码生成时间: 2025-08-30 13:46:59
import scrapy
def is_empty(value):
    """
    Check if the value is None or empty string.
    """
    return value is None or value == ''
def is_integer(value):
    """
    Check if the value is an integer.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
def is_positive_integer(value):
    """
    Check if the value is a positive integer.
    """
    return is_integer(value) and int(value) > 0
def is_email(value):
    """
    Check if the value is a valid email address.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, value) is not None
def validate_form_data(data):
    """
    Validate the form data.
    
    Args:
        data (dict): The form data to be validated.
            Example: {'name': 'John', 'age': '30', 'email': 'john@example.com'}
    
    Returns:
        dict: A dictionary containing the errors.
            If no errors are found, an empty dictionary is returned.
    """
    errors = {}
    
    # Validate name
    if is_empty(data.get('name', '')):
        errors['name'] = 'Name is required'
    elif not isinstance(data['name'], str):
        errors['name'] = 'Name must be a string'
    
    # Validate age
    if is_empty(data.get('age', '')):
        errors['age'] = 'Age is required'
    elif not is_positive_integer(data['age']):
        errors['age'] = 'Age must be a positive integer'
    
    # Validate email
    if is_empty(data.get('email', '')):
        errors['email'] = 'Email is required'
    elif not is_email(data['email']):
        errors['email'] = 'Invalid email address'
    
    return errors
def main():
    """
    Main function to test the form data validator.
    """
    data = {
        'name': 'John Doe',
        'age': '30',
        'email': 'john@example.com'
    }
    errors = validate_form_data(data)
    if errors:
        print('Errors:')
        for field, error in errors.items():
            print(f'{field}: {error}')
    else:
        print('Validation successful')
def __is_main():
    main()
if __name__ == '__main__':
    __is_main()