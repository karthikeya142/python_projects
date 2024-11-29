from fpdf import FPDF
pdf=FPDF()
#first page
pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5,"To find out what's new in tutorials, click")
pdf.set_font(style="U")
link =pdf.add_link(page=1)
pdf.write(5,"here",link)

#second page
pdf.add_page()
pdf.image("logo.png",10,10,50,0,"","https://www.google.com")
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html(""" my name karthik <b> this is karthikeya </b>
                <h1> this is heading </h1>
                <a href="https://www.google.com">click here to google </a>
                """)
pdf.output("link.pdf")