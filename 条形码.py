import barcode
from barcode.writer import ImageWriter
def barcode_to_png(barcode_type,text_str,filename):
    EAN = barcode.get_barcode_class(barcode_type)
    ean = EAN(text_str, writer = ImageWriter())
    ean.save(filename)
i=1
code = 692127930000 + i
for i in range(1,5):
    if __name__ == "__main__":
        barcode_to_png('ean13',str(code),'barcode0'+str(i))