def emailValida(email):
    if '@gmail.com' in email or '@hotmail.com' in email or '@outlook.com' in email:
        return True
    else:
        return False
