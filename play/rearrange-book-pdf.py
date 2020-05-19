import PyPDF2 as pdf
## open book pdf
pdfBookObj = open('/Users/diogovalentepcs/Documents/play/RedDragon_ThomasHarris.pdf', 'rb')
# creating a pdf reader object 
pdfBookReader = pdf.PdfFileReader(pdfBookObj)


numPages = pdfBookReader.numPages
insertPosition = 0
book =[]

for i in range(0,numPages):
    book.append(i)

lastPage = numPages-1
page = book[lastPage]
## shift pages forward from insertPosition until last
for x in range(lastPage-1,insertPosition-1,-1):
    book[x+1] = book[x]
##insert lastpage in insertPosition
book[insertPosition] = page
insertPosition += 3

while insertPosition + 1 < numPages :
    ## insert
    for i in range(2):
        page = book[lastPage]
        ## shift pages forward from insertPosition until last
        for x in range(lastPage-1,insertPosition-1,-1):
            book[x+1] = book[x]
        ##insert lastpage in insertPosition
        book[insertPosition] = page
        insertPosition += 1
    insertPosition += 2


output = pdf.PdfFileWriter()
for i in range(len(book)):
    # creating a page object that gets the page with the rearrenged number
    pageObj = pdfBookReader.getPage(book[i])
    output.addPage(pageObj)

outputFile = open('/Users/diogovalentepcs/Documents/play/PrintBook.pdf', 'wb')
output.write(outputFile)
