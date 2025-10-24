# trying out pypdf
if __name__ == "__main__":
    import pypdf
    from pathlib import Path

    with open(Path("resources/pdf_merge/dummy.pdf"), "rb") as file:
        reader = pypdf.PdfReader(file)

        print(reader.get_num_pages())
        print(reader.get_page(0))

        page = reader.get_page(0)  # assign first page to variable page
        print(page.rotate(90))  # this doesn't save the page rotated

        writer = pypdf.PdfWriter()
        writer.add_page(page.rotate(90))

        with open(Path("resources/pdf_merge/rotated.pdf"), "wb") as rotated_file:
            writer.write(rotated_file)
