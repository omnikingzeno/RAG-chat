import os

def load_documents(folder_path = "data/documents") :
    """Load and return all text files from above directory"""

    documents = []
    if not os.path.exists(folder_path) :
        os.makedirs(folder_path) #create all directories written in the folder's path
        print(f"Created folder at {folder_path}. Add documents in this directory.")
        return documents

    for filename in os.listdir(folder_path) :
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".txt") :
            with open(file_path, 'r', encoding = 'utf-8') as file :
                documents.append(file.read())
    return documents