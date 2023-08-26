from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import streamlit as st
from PIL import Image, PngImagePlugin
import io

load_dotenv(find_dotenv())


@st.cache
def imgDetection(url):
    object_detection = pipeline("object-detection", model="facebook/detr-resnet-50")

    results = object_detection(url)
    return results


@st.cache
def imgToText(url):
    object_detection = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    results = object_detection(url)[0]["generated_text"]
    return results


def add_metadata(image, labels, text_description):
    # Convert image to PNG format to support metadata
    png_image = Image.new("RGB", image.size)
    png_image.paste(image)

    # Create PNG info dictionary with labels
    info = PngImagePlugin.PngInfo()
    info.add_text("Detected_Labels", ", ".join(labels))
    info.add_text("Text_Description", text_description)

    # Save image with metadata
    output_image = io.BytesIO()
    png_image.save(output_image, format="PNG", pnginfo=info)
    output_image.seek(0)

    return output_image


def main():
    st.title("Image Detection (Write Metadata)")

    uploaded_file = st.file_uploader("Choose a file...", type=["jpg", "png", "jpeg"])  # jpg, jpeg, png

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        original_file_name = uploaded_file.name

        # Resize down to original aspect ratio
        image.thumbnail((500, 500))

        # Display the uploaded image as a preview
        st.image(image, caption="Uploaded Image", use_column_width=True)

        detection_results = imgDetection(image)

        st.write("Detected Scenery:")
        description = imgToText(image).capitalize() + "."
        st.write(description)

        st.write("Detected Objects:")
        selected_labels = []
        displayed_labels = set()  # To track displayed labels

        num_columns = 3
        cols = st.columns(num_columns)

        checkbox_index = 0  # Index to track the current checkbox

        for result in detection_results:
            label = result["label"].lower()  # Convert label to lowercase

            # Display checkbox only if label is not already displayed
            if label not in displayed_labels:
                checkbox_key = f"checkbox_{label}"  # Use label as the key
                displayed_labels.add(label)  # Add the label to the displayed set

                checkbox_column = cols[checkbox_index % num_columns]  # Choose the appropriate column
                checkbox = checkbox_column.checkbox(result["label"], key=checkbox_key)

                if checkbox:
                    selected_labels.append(label)

                checkbox_index += 1  # Move to the next checkbox index

        if selected_labels:
            st.write("Selected Labels:", selected_labels)

            modified_image = add_metadata(image, selected_labels, description)

            st.download_button(
                label="Download Image with Metadata",
                data=modified_image,
                file_name=original_file_name,
                mime="image/png"
            )


if __name__ == "__main__":
    main()