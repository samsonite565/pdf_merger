from PyPDF2 import PdfMerger
import re
import os


def main():
    pdf_nums = int(
        input("How many pdfs do you have? Please enter a number. ")
    )
    files = []
    for n in range(0, pdf_nums):
        try:
            path = input(
                "Please enter the file path for pdf \n[Please remove the quotes from the path when copying]"
            ).strip('"')
        except FileNotFoundError:
            print("File not found. Please check the path.")
        else:
            file.append(path)
    print(file)
    mergefile(file)


def mergefile(files):

    with open("month_name.pdf", mode="wb") as new_file:
        merger = PdfMerger()
        for pdf in files:
            merger.append(pdf)
        merger.write(new_file)
        merger.close()
    os.startfile("month_name.pdf")


if __name__ == "__main__":
    main()
