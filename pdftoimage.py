import pandas as pd
import pytesseract as pt
import pdf2image

# Read a pdf file as image pages (A4 size)
pages = pdf2image.convert_from_path(pdf_path='Ticket2021-02-08.pdf', dpi=200, size=(1654, 2340))
content = pt.image_to_string(pages[0], lang='spa')

#  Only cut description part
front_part = content.split('IMPORTE')[1]
text = front_part.split('SUBTOTAL')[0]

#  Separate every line
lines = text.split('\n')

data = []
for line in lines[1:-1]:
    line_list = line.split()

    if 'KG' in line_list:
        cantidad = line_list[line_list.index('KG')-1] + 'kg'
        del line_list[line_list.index('KG')-1]
        line_list.remove('KG')
    elif 'kg' in line_list:
        cantidad = line_list[line_list.index('kg')-1] + 'kg'
        del line_list[line_list.index('kg') - 1]
        line_list.remove('kg')
    elif 'GR.' in line_list:
        cantidad = line_list[line_list.index('GR.') - 1] + 'g'
        del line_list[line_list.index('GR.') - 1]
        line_list.remove('GR.')
    elif 'GR' in line_list:
        cantidad = line_list[line_list.index('GR') - 1] + 'g'
        del line_list[line_list.index('GR') - 1]
        line_list.remove('GR')
    else:
        cantidad = ''

    if '€/kg' in line_list:
        pvp = line_list[line_list.index('€/kg') - 1] + '€/kg'
        del line_list[line_list.index('€/kg') - 1]
        line_list.remove('€/kg')
    else:
        pvp = ''

    euro = line_list[-1]
    del line_list[-1]
    articulo = ' '.join(line_list)
    data.append([articulo, cantidad, pvp, euro])
df = pd.DataFrame(data, columns=['Articulo', 'Cantidad', 'PVP/UNIT', '€'])
df.to_excel('output.xlsx')
print(df)

