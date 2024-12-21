from ebooklib import epub
from bs4 import BeautifulSoup
import os

def extract_images_with_page_numbers(epub_path, output_folder):
    # Load the EPUB book
    book = epub.read_epub(epub_path)

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize page count
    page_number = 1

    # Iterate over the spine, which gives the order of reading
    for item in book.get_items_of_type(9):
        # Parse the HTML content
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')

        # Find all image tags in the document
        for img in soup.find_all('img'):
            # Get the image path
            image_path = img.get('src')

            # Retrieve the image item by its name
            image_item = book.get_item_with_href(image_path)

            if image_item:
                # Construct the output filename with the page number
                output_filename = f"{page_number}.png"  # Adjust the format as needed

                # Determine the output path for the image
                output_path = os.path.join(output_folder, output_filename)

                # Write the image data to a file
                with open(output_path, 'wb') as image_file:
                    image_file.write(image_item.get_content())

                print(f"Extracted image to {output_path}")

            # Increment the page number for each image found
            page_number += 1

def create_directories_for_epubs(directory_path):
    # Ensure the directory_path is valid
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path {directory_path} is not a valid directory.")

    # Iterate over all files in the given directory
    for filename in os.listdir(directory_path):
        # Check if the file has an .epub extension
        if filename.endswith('.epub'):
            # Create a directory name by removing the .epub suffix
            dir_name = filename[:-5]  # Remove the '.epub' suffix
            dir_path = os.path.join(directory_path, dir_name)
            # Create the directory if it doesn't already exist
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"Created directory: {dir_path}")
            else:
                print(f"Directory already exists: {dir_path}")

def extract_images_of_epubs(directory_path):
    # Ensure the directory_path is valid
    if not os.path.isdir(directory_path):
        raise ValueError(f"The path {directory_path} is not a valid directory.")

    # Iterate over all files in the given directory
    for filename in os.listdir(directory_path):
        # Check if the file has an .epub extension
        if filename.endswith('.epub'):
            # Create a directory name by removing the .epub suffix
            dir_name = filename[:-5]  # Remove the '.epub' suffix
            dir_path = os.path.join(directory_path, dir_name)
            # Create the directory if it doesn't already exist
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"Created directory: {dir_path}")
            else:
                print(f"Directory already exists: {dir_path}")
            extract_images_with_page_numbers(filename, dir_path)

# Example usage
# epub_file_path = '1.epub'
# output_directory = 'test2'
# extract_images_with_page_numbers(epub_file_path, output_directory)
current_directory = os.getcwd()
extract_images_of_epubs(current_directory)