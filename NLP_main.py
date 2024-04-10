from PIL import Image
import easyocr
import os

def create_unique_filename(base_name, path, extension):
  """
  Creates a unique filename by incrementing a numerical suffix until a non-existent file is found.
  """
  i = 1
  while True:
    try:
      filename = f"{base_name}{i}{extension}"
      full_path = os.path.join(path, filename)
      if not os.path.exists(full_path):
        return full_path
      i += 1

    except ValueError as e:
      print(f"Error: {e}")

def write_text_to_file(text_lines, filename):
  """
  Writes the extracted text lines to a new or existing .txt file.
  """
  with open(filename, 'w', encoding='utf-8') as file:
    for line in text_lines:
      file.write(line + '\n')  # Write each line with a newline character

while True:
  try:
    # Get input for file paths
    file_path = input("Enter the path where you want to save the .txt files: ").rstrip("\\/")
    file_path = file_path.strip()  # Remove leading/trailing spaces
    image_path = input("Enter the path to the image file: ").rstrip("\\/")
    image_path = image_path.strip()  # Remove leading/trailing spaces

    # Verify if paths exist
    if not os.path.exists(file_path):
      raise ValueError("Output path does not exist. Please enter a valid path.")
    # Verify if the image file exists
    if not os.path.isfile(image_path):
      raise ValueError("Image file does not exist. Please enter a valid filepath.")

    break  # Paths are valid, exit the loop

  except ValueError as e:
    print(f"Error: {e}")
# Use a pre-trained model for text detection (reader: 'en')
reader = easyocr.Reader(['en'])  # Change language code for different languages

# Read the image and extract text using easyocr (using file path)
try:
  img = Image.open(image_path)  # Optional (for verification)
  results = reader.readtext(image_path)

  # Extract all text lines from the results
  extracted_text_lines = [result[1] for result in results]

  # Create a unique filename based on the image filename
  base_name, _ = os.path.splitext(os.path.basename(image_path))  # Extract filename without extension
  txt_filename = create_unique_filename(base_name, file_path, ".txt")

  # Write the extracted text to the .txt file
  write_text_to_file(extracted_text_lines, txt_filename)
  print(f"Text extracted and saved to: {txt_filename}")

except Exception as e:
  print(f"Error: {e}")
