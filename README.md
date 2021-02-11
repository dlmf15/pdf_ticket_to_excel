# pdf_ticket_to_excel
Extract text from a grocery ticket pdf. Output in Excel.(Supermarket in Spain "Día")

This ticket pdf is an image, which you cannot copy text from pdf Reader.

Used system: MacOS Big Sur version 11.2

Tested python version: 3.8, 3.7, 3.6

## Requirements
Need to install tesseract and poppler.


In terminal:
```
brew install tesseract
```
And tesseract languages packs: 
(Here is spanish in the ticket)
```
tesseract --list-langs
```
poppler:
```
brew install poppler
```

Python packages:
```
pandas
pytesseract
pdf2image
openpyxl
```

## Results

![alt text](https://github.com/dlmf15/pdf_ticket_to_excel/blob/master/Screenshot.png)
