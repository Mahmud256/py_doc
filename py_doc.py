from docx import Document
import os

def add_list_symbol(doc_path):
    # Load the Word document
    doc = Document(doc_path)

    # Iterate through each paragraph
    for paragraph in doc.paragraphs:
        # Check if the paragraph starts with a bullet point symbol ('•')
        if paragraph.text.startswith('•'):
            # Remove the bullet point symbol and add an asterisk symbol before the paragraph
            paragraph.text = '* ' + paragraph.text[2:]
        # Check if the paragraph ends with a vertical bar
        elif paragraph.text.endswith('|'):
            # Add a dash symbol before the paragraph
            paragraph.text = '- ' + paragraph.text
        # Check if the paragraph ends with a question mark
        elif paragraph.text.endswith('?'):
            # Add an asterisk symbol before the paragraph
            paragraph.text = '* ' + paragraph.text
        elif paragraph.text.endswith(':'):
            # Add a colon symbol before the paragraph
            paragraph.text = '* ' + paragraph.text

    # Save the modified document
    modified_doc_path = 'modified_' + doc_path
    doc.save(modified_doc_path)
    print(f"Modified document saved as '{modified_doc_path}'")

    # Open the modified document
    os.system(f'start {modified_doc_path}')

# Call the function to add list symbols
add_list_symbol('example.docx')
