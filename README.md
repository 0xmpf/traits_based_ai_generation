
# README
This Python script generates portrait pictures based on various human traits using AI. It can be used as a sample application or adapted for various image generation projects. The original goal is to generate NFT collection generated by AI but with traits.

# Features

- Randomly selects traits such as origin, religion, hair length, color, style, character, gender, age, accessories, and occupation.

- Creates a custom prompt based on the chosen traits to guide the image generation process.
  
- Generates multiple portrait images with the selected traits using a pre-trained model.
Saves the generated images as PNG files with unique names.

- Writes the chosen traits for each image to a JSON file for reference.

# Requirements

- Python 3.x
- diffusers library
- torch library

# Usage

## Install the required libraries:
    pip install diffusers torch accelerate

Update the path variable in the script with the path to your desired model (default is 'fluently/Fluently-XL-v4').

Customize the negative_prompt if you want to add any specific elements to avoid in the generated images.
Set the number of generations you want by modifying the n variable.

**Run the appropriate script based on your system**:

For CUDA-enabled systems (GPU), use generate_cuda.py:
    
    python generate_cuda.py

For macOS systems (CPU), use generate_macos.py:
 
    python generate_macos.py


The generated portrait images will be saved as PNG files, and the chosen traits for each image will be written to a JSON file.

## Jupyter Notebook
If you have limited GPU resources or prefer using Google Colab, you can use the provided Jupyter Notebook (generate_portraits.ipynb) to run the script. Simply upload the notebook to Google Colab and follow the instructions within the notebook.

### Customization

You can customize the script by modifying the traits.json file to add, remove, or adjust the traits and their chances. The script will randomly select traits based on the defined probabilities.

# Contributions

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. Make sure to follow the existing code style and provide clear descriptions of your changes.
