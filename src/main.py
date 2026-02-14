from text_extraction import extract_text_from_pdf
from preprocessing import normalize


def main():
    file_path = "../data/sample_resume.pdf"
    resume_text = extract_text_from_pdf(file_path)

    print("Extracted Resume Text:\n")
    print(resume_text)

    print("NORMALIZED:\n")
    resume_norm = normalize(resume_text)
    print(resume_norm)


if __name__ == "__main__":
    main()
