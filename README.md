# Image Detection (Write Metadata) Streamlit App

This Streamlit app allows you to upload images, detect objects in them, generate text descriptions, and add metadata to the images.

## Getting Started

Follow these steps to set up and run the Streamlit app on your local machine.

### Prerequisites

- Python (>=3.9)
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/timooo-thy/imageDetection.git
   cd imageDetection

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   
3. Install the required packages:

   ```bash
   pip install -r requirements.txt

### Setup Environment Variables

1. Create a `.env` file in the root directory of the project.

2. Add your huggingface token information to the `.env` file in the following format:
   HUGGINGFACEHUB_API_TOKEN = your_api_key_here

3. Make sure to include `.env` in your `.gitignore` file to keep your sensitive information secure.

### Running the App

1. Open a terminal and navigate to the project directory.

2. Activate the virtual environment if you created one:

   ```bash
   source venv/bin/activate # On Windows: venv\Scripts\activate
   
3. Run the Streamlit app:

   ```bash
   streamlit run app.py

4. The app should open in your default web browser.

## Deploying to Production

For deploying the app to a production environment, consider using platforms like Heroku or GitHub Pages. Be sure to adjust configurations and follow deployment instructions for your chosen platform.
