#Libs necessarias
from googletrans import Translator
from PIL import Image, ImageOps, ImageFilter
import pytesseract
import pyscreenshot as ImageGrab
#import spacy

def main():
    #Capturando tela
    img = ImageGrab.grab().crop((75,100,900,600))

    #Translator
    translator = Translator()

    #Entendo o idioma
    #nlp = spacy.load('pt')

    #ORC dentro do sistema
    #Tive que instalar este programa para fazer o OCR funcionar, instale se quiser que o bagulho funcione
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    #imagem 
    #img = Image.open('teste.png')
    #img = Image.open('teste1.PNG')
    #img = Image.open('teste2.PNG')
    #img = Image.open('teste3.PNG')

    #Invertendo as cores da imagem
    #Nao funcionou com imagem capturada
    """
    r,g,b,a = img.split()
    imagem_RGB = Image.merge('RGB', (r,g,b))
    inverted_image = ImageOps.invert(imagem_RGB)
    r,g,b = inverted_image.split()
    img = Image.merge('RGB', (r,g,b))
    """

    #Invertendo as cores da imagem
    img = ImageOps.invert(img)

    #Convertendo a imagem para a escala de cinza
    img = img.convert('L')

    #Convertendo a imagem para a escala de 2 bits
    img = img.quantize(2,1)

    #Equalizando a imagem
    img = ImageOps.equalize(img)

    #Filtro box comum
    k = [1,1,1,1,1,1,1,1,1]
    filtro = ImageFilter.Kernel((3,3),k)
    img1 = img.filter(filtro)

    x = 0
    img3 = img
    while True:
        img3 = img3.filter(filtro)
        if x == 3:
            break
        else:
            img2 = img3.filter(filtro)
        x=x+1
        
    #Aplicando um gausiano 3x3
    k = [1,2,1,2,4,2,1,2,1]
    filtro = ImageFilter.Kernel((3,3),k)
    img4 = img.filter(filtro)

    x = 0
    img6 = img
    while True:
        img6 = img6.filter(filtro)
        if x == 3:
            break
        else :
            img5 = img6.filter(filtro)
        x=x+1

    #Salvando a imagem para verificar o estado
    """
    img1.save("saida1.png")
    img2.save("saida2.png")
    """

    #Printando a traducao
    arquivo = open("texto.txt", "w+")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 1")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img1), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 2")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img2), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 3")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img3), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 4")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img4), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 5")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img5), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write("Traducao - 6")
    arquivo.write("\n--------------------------------------------------\n")
    arquivo.write(translator.translate(pytesseract.image_to_string(img6), dest='pt').text)
    arquivo.write("\n--------------------------------------------------\n")

if __name__ == "__main__":
    main()
