import os
import shutil

root = 'E:/Project/Freelance-Projects/Blog/blog_site'

# List of directories to delete
directories_to_delete = ['__pycache__', 'migrations']

def delete_directories(root, directories):
    for dirpath, dirnames, filenames in os.walk(root):
        for dirname in dirnames:
            if dirname in directories:
                dir_to_delete = os.path.join(dirpath, dirname)
                print(f"Deleting directory: {dir_to_delete}")
                shutil.rmtree(dir_to_delete, ignore_errors=True)

if __name__ == "__main__":
    delete_directories(root, directories_to_delete)
        
