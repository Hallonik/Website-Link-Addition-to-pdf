#to add links to pdf pages which connects various pages
#as well as websites along with adding links to images 
#also adding html codes


from fpdf import FPDF

pdf=FPDF()

#1st page
pdf.add_page()
pdf.set_font("times",size=20)

pdf.write(5,"To find out how to impress your crush in 100 ways,click")#to write a statement before
#the given link to be added
pdf.set_font(style="U")
link=pdf.add_link(page=2)#to add the link
pdf.write(5," here",link)
#now the first page is created with a link to the 2nd page



#second page
pdf.add_page()
 
    #adding an image along with a link to that image
pdf.image("im.png",10,10,50,0,"","https://www.aniwatch.to")

pdf.set_left_margin(60)#settng the left margin for html
pdf.set_font_size(18)#setting the font
pdf.write_html("<b>This is some bold text</b>")
pdf.write_html("""You can add html code here<b>This text is bold</b>
               <h1>This is heading</h1>
               <a href="https://facebook.com">Click here to go to fb</a>"
               
               """)#to add html codes to pdf

#creating the pdf
pdf.output("link.pdf")

