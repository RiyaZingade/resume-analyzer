from text_extraction import extract_text_from_pdf


def main():
    file_path = "../data/sample_resume.pdf"
    resume_text = extract_text_from_pdf(file_path)

    print("Extracted Resume Text:\n")
    print(resume_text)


if __name__ == "__main__":
    main()
