import os
import glob
import shutil


def clean_files(file_patterns):
    # Get the current working directory
    current_dir = os.getcwd()

    for pattern in file_patterns:
        # Find all files matching the pattern under the current directory and its subdirectories
        files_to_delete = glob.glob(
            os.path.join(current_dir, "**", pattern), recursive=True
        )

        # Delete each found file
        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except OSError as e:
                print(f"Error deleting {file}: {e}")


def clean_directories(dir_patterns):
    # Get the current working directory
    current_dir = os.getcwd()

    for pattern in dir_patterns:
        # Find all directories matching the pattern under the current directory and its subdirectories
        dirs_to_delete = glob.glob(
            os.path.join(current_dir, "**", pattern), recursive=True
        )

        # Delete each found directory
        for directory in dirs_to_delete:
            try:
                shutil.rmtree(directory)
                print(f"Deleted directory: {directory}")
            except OSError as e:
                print(f"Error deleting directory {directory}: {e}")


if __name__ == "__main__":
    # List of file patterns to clean up
    file_patterns = ["tempCodeRunnerFile.py", "*.log", "*.tmp"]
    clean_files(file_patterns)

    # List of directory patterns to clean up
    dir_patterns = ["__pycache__", ".pytest_cache"]
    clean_directories(dir_patterns)
