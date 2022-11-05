from pdf2docx import Converter


def main():
    pdf_file = 'rickroll_4k.pdf'
    docx_file = 'rickroll_4k.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


if __name__ == '__main__':
    main()
