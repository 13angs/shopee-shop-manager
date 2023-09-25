import PyPDF2, uuid, os

# Create a PDF merger object

def merge_all_pdfs(dir: str, pdf_files: list) -> list:
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through the list of PDF files and append them to the merger
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # Specify the output PDF file
    pdf_name = '{}.{}'.format(str(uuid.uuid1()), 'pdf')
    output_pdf = os.path.join(dir, pdf_name)

    # Write the merged PDF to the output file
    with open(output_pdf, 'wb') as output_file:
        pdf_merger.write(output_file)

    # Close the merger
    pdf_merger.close()

    print(f'Merged {len(pdf_files)} PDF files into {output_pdf}')
    return [pdf_name, output_pdf]