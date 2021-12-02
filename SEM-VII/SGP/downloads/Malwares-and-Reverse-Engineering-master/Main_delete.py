# importing the required modules
import os
import shutil
import time
import threading


# main function
def main():
    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    # specify the path
    path = "C:\\Users\\HP\\Desktop\\Delete all"

    # specify the days
    days = 0

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present in path or not
    if os.path.exists(path):

        # iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):

            # comparing the days
            if seconds >= get_file_or_folder_age(root_folder):

                # removing the folder
                remove_folder(root_folder)
                deleted_folders_count += 1  # incrementing count

                # breaking after removing the root_folder
                break

            else:

                # checking folder from the root_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    # comparing with the days
                    if seconds >= get_file_or_folder_age(folder_path):
                        # invoking the remove_folder function
                        remove_folder(folder_path)
                        deleted_folders_count += 1  # incrementing count

                # checking the current directory files
                for file in files:

                    # file path
                    file_path = os.path.join(root_folder, file)

                    # comparing the days
                    if seconds >= get_file_or_folder_age(file_path):
                        # invoking the remove_file function
                        remove_file(file_path)
                        deleted_files_count += 1  # incrementing count

        else:

            # if the path is not a directory
            # comparing with the days
            if seconds >= get_file_or_folder_age(path):
                # invoking the file
                remove_file(path)
                deleted_files_count += 1  # incrementing count

    else:

        # file/folder is not found
        print(f'"{path}" is not found')
        deleted_files_count += 1  # incrementing count

    print(f"Total folders deleted: {deleted_folders_count}")
    print(f"Total files deleted: {deleted_files_count}")
    time.sleep(1)


def remove_folder(path):
    # removing the folder
    if not shutil.rmtree(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # failure message
        print(f"Unable to delete the {path}")


def remove_file(path):
    # removing the file
    if not os.remove(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # failure message
        print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime

    # returning the time
    return ctime


########################################################################################

# function that returns size of a file
def get_file_size(path):
    # getting file size in bytes
    size = os.path.getsize(path)

    # returning the size of the file
    return size


# function to delete a file


def main_1():
    # specify the path
    path = "C:\\Users\\HP\\Desktop\\dellele"

    # put max size of file in MBs
    size = 0

    # checking whether the path exists or not
    if os.path.exists(path):

        # converting size to bytes
        size = size * 1024 * 1024

        # traversing through the subfolders
        for root_folder, folders, files in os.walk(path):

            for folder in folders:
                file_path1 = os.path.join(root_folder, folder)

                if get_file_size(file_path1) >= size:
                    remove_folder(file_path1)

            # iterating over the files list

            for file in files:

                # getting file path
                file_path = os.path.join(root_folder, file)

                # checking the file size
                if get_file_size(file_path) >= size:
                    # invoking the remove_file function
                    remove_file(file_path)


        else:

            # checking only if the path is file
            if os.path.isfile(path):

                # path is not a dir
                # checking the file directly
                if get_file_size(path) >= size:
                    # invoking the remove_file function
                    remove_file(path)



    else:

        # path doesn't exist
        print(f"{path} doesn't exist")
    time.sleep(1)


t1 = threading.Thread(target=main)
t2 = threading.Thread(target=main_1)

t1.start()
t2.start()
