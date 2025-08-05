import os
import ast

folder_path = f'{os.getcwd()}/data'
file_name = 'products.txt'
complete_path = folder_path +'/'+ file_name

def is_file_created():
    if not os.path.exists(folder_path):
        try:
            os.mkdir(folder_path)
            open(complete_path, 'x')
        except OSError as error:
            print(error)
            return False

    elif not os.path.exists(complete_path):
        try: 
            open(complete_path, 'x')
        except Exception as error:
            print(error)
            return False

    return True


def getData():
    if is_file_created():
        try: 
            with open(complete_path, 'r') as x:
                content = x.read()
                if(content.replace(' ', '') == ''):
                    return {}
                return ast.literal_eval(content)            
        except FileNotFoundError:
            print("Error: The file was not found")
        except Exception as e: 
            print(f"Error: {e}")

def setData(data: dict):
    if is_file_created():
        try:
            with open(complete_path, 'w') as file:
                file.write(str(data))
            print("Guardado correctamente")
        except FileNotFoundError:
            print("Error: The file was not found")
        except Exception as e: 
            print(f"Error: {e}")
