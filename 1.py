import os
import json
import xml.etree.ElementTree as ET
import zipfile

def list_files(directory):
    """List all files in the specified directory excluding .zip files and .DS_Store."""
    try:
        print(f"Accessing directory: {directory}")  
        files = [
            f for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f)) 
            and not f.endswith('.zip') 
            and f != '.DS_Store'  # исключаем .DS_Store
        ]
        print(f"Files found: {files}")  
        if not files:
            print("No files found in the directory.")
        return files
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
        return []

def write_to_file(file_path, content):
    """Write content to a text file."""
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"File successfully created and content written: {content}")

def read_file(file_path):
    """Read content from a text file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(f"Content of the file:\n{content}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

def delete_file(file_path):
    """Delete a file."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File successfully deleted: {file_path}")
    else:
        print("File does not exist.")

def create_json(file_path, data):
    """Create a JSON file with the given data."""
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
    print(f"JSON file successfully created: {file_path}")

def read_json(file_path):
    """Read content from a JSON file."""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        print(f"Content of the JSON file:\n{data}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"Error reading JSON file: {e}")

def delete_json(file_path):
    """Delete a JSON file."""
    delete_file(file_path)

def create_xml(file_path, data):
    """Create an XML file with the given data."""
    root = ET.Element("root")
    data_element = ET.SubElement(root, "data")
    data_element.text = data
    tree = ET.ElementTree(root)
    tree.write(file_path)
    print(f"XML file successfully created: {file_path}")

def read_xml(file_path):
    """Read content from an XML file."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = root.find("data").text
        print(f"Content of the XML file:\n{data}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ET.ParseError:
        print("Error parsing XML.")
    except Exception as e:
        print(f"Error reading XML file: {e}")

def delete_xml(file_path):
    """Delete an XML file."""
    delete_file(file_path)

def create_zip(zip_path, file_paths):
    """Create a zip archive containing the specified files."""
    try:
        with zipfile.ZipFile(zip_path, 'a') as zipf:
            for file_path in file_paths:
                zipf.write(file_path, os.path.basename(file_path))
                print(f"File {file_path} successfully added to zip archive: {zip_path}")
                os.remove(file_path)  # Remove the original file after zipping
    except Exception as e:
        print(f"Error creating zip: {e}")

def unzip(zip_path, extract_path):
    """Unzip the specified zip file to the extract path."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Contents of the archive extracted: {zip_path}")
        os.remove(zip_path)  # Remove the zip file after extracting
    except FileNotFoundError:
        print(f"Zip file not found: {zip_path}")
    except zipfile.BadZipFile:
        print("Error: Bad zip file.")
    except Exception as e:
        print(f"Error extracting zip: {e}")

def main():
    print("Starting the program...")  
    directory = "/Users/slayyyter/Desktop/Папки С Учебой/7sem/rzrbbezpo"
    
    while True:
        print("\nMenu:")
        print("1. List files")
        print("2. Write to text file")
        print("3. Read text file")
        print("4. Delete text file")
        print("5. Create JSON file")
        print("6. Read JSON file")
        print("7. Delete JSON file")
        print("8. Create XML file")
        print("9. Read XML file")
        print("10. Delete XML file")
        print("11. Create ZIP archive")
        print("12. Unzip file")
        print("13. Exit")
        
        choice = input("Choose an option (1-13): ")
        
        if choice == '1':
            print("Listing files...")  
            files = list_files(directory)
            if files:
                print("Select files to perform operations:")
                for i, file in enumerate(files, start=1):
                    print(f"{i}. {file}")
            else:
                print("No files found in the directory.")
            input("Press Enter to return to the menu...")
            
        elif choice == '2':
            filename = input("Enter filename (without extension): ")
            content = input("Enter content to write: ")
            write_to_file(os.path.join(directory, f"{filename}.txt"), content)
            input("Press Enter to return to the menu...")
            
        elif choice == '3':
            filename = input("Enter filename (without extension): ")
            read_file(os.path.join(directory, f"{filename}.txt"))
            input("Press Enter to return to the menu...")
            
        elif choice == '4':
            filename = input("Enter filename (without extension): ")
            delete_file(os.path.join(directory, f"{filename}.txt"))
            input("Press Enter to return to the menu...")
            
        elif choice == '5':
            filename = input("Enter filename (without extension): ")
            data = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}
            create_json(os.path.join(directory, f"{filename}.json"), data)
            input("Press Enter to return to the menu...")
            
        elif choice == '6':
            filename = input("Enter filename (without extension): ")
            read_json(os.path.join(directory, f"{filename}.json"))
            input("Press Enter to return to the menu...")
            
        elif choice == '7':
            filename = input("Enter filename (without extension): ")
            delete_json(os.path.join(directory, f"{filename}.json"))
            input("Press Enter to return to the menu...")
            
        elif choice == '8':
            filename = input("Enter filename (without extension): ")
            data = input("Enter data to write in XML: ")
            create_xml(os.path.join(directory, f"{filename}.xml"), data)
            input("Press Enter to return to the menu...")
            
        elif choice == '9':
            filename = input("Enter filename (without extension): ")
            read_xml(os.path.join(directory, f"{filename}.xml"))
            input("Press Enter to return to the menu...")
            
        elif choice == '10':
            filename = input("Enter filename (without extension): ")
            delete_xml(os.path.join(directory, f"{filename}.xml"))
            input("Press Enter to return to the menu...")
            
        elif choice == '11':
            zip_filename = input("Enter zip filename (without extension): ")
            print("Select files to zip (enter numbers separated by spaces):")
            files_to_zip = list_files(directory)
            if not files_to_zip:
                print("No files available to zip.")
                input("Press Enter to return to the menu...")
                continue
            for i, file in enumerate(files_to_zip, start=1):
                print(f"{i}. {file}")
            selected_files = input("Enter your choices: ")
            selected_indices = map(int, selected_files.split())
            file_paths = [os.path.join(directory, files_to_zip[i-1]) for i in selected_indices if 1 <= i <= len(files_to_zip)]
            create_zip(os.path.join(directory, f"{zip_filename}.zip"), file_paths)
            input("Press Enter to return to the menu...")
            
        elif choice == '12':
            zip_filename = input("Enter zip filename (without extension): ")
            unzip(os.path.join(directory, f"{zip_filename}.zip"), directory)
            input("Press Enter to return to the menu...")
            
        elif choice == '13':
            print("Exiting the program.")
            break
            
        else:
            print("Invalid option, please choose again.")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
