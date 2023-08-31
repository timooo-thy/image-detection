# Image Detection (Write Metadata) Streamlit App

Welcome to the Image Detection (Write Metadata) Streamlit App!

With this Streamlit app, you can easily:

-Upload images

-Detect objects within them

-Generate text descriptions

-Add metadata to the images

The models employed in this app are sourced from [Hugging Face](https://huggingface.co) and include "facebook/detr-resnet-50" for object detection and "Salesforce/blip-image-captioning-base" for text generation.

## Getting Started

Follow these steps to set up and run the Streamlit app on your local machine.

## Prerequisites

- Python (>=3.9)
- pip (Python package manager)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/timooo-thy/image-detection.git
   cd image-detection

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   
3. Install the required packages:

   ```bash
   pip install -r requirements.txt

## Setup Environment Variables

1. Create a `.env` file in the root directory of the project.

2. Add your huggingface token information to the `.env` file in the following format:
   HUGGINGFACEHUB_API_TOKEN = your_api_key_here

3. Make sure to include `.env` in your `.gitignore` file to keep your sensitive information secure.

## Running the App

1. Open a terminal and navigate to the project directory.

2. Activate the virtual environment if you created one:

   ```bash
   source venv/bin/activate # On Windows: venv\Scripts\activate
   
3. Run the Streamlit app:

   ```bash
   streamlit run app.py

4. The app should open in your default web browser.

## Deploying to Production

For deploying the app to a production environment, consider deploying from Streamlit. Be sure to adjust configurations and follow deployment instructions for your chosen platform.
