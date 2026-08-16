from fpdf import FPDF 


def main():
    # create a pdf and add page to it, inside this page we insert the shirt image 
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirt.png", x=10, y=70, w=190)

    # set CS50 Shirtificate title
    pdf.set_y(20)
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")

    # take the name from the user and set the white colour for the text, set type of font
    name = input("Name: ")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("times", "B", 24)

    # set the text position, print text in the pdf 
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50P", align="C")
 
    # save pdf as shirtificate.pdf
    pdf.output("shirtificate.pdf")


if __name__=="__main__":
    main()