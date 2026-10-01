import numpy as np
import cv2
# Vision artificial Act10 NC = 0039
# Lee la imagen en escala de grises
Img = cv2.imread("triple t.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("TripleT 0039", Img)
cv2.waitKey(0)
cv2.destroyAllWindows


# Linea
print("La linea 0039")
# Crea una imagen negra
iMg = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
iMg = cv2.line(iMg,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("Line 0039", iMg)
cv2.waitKey(0)
cv2.destroyAllWindows


# Circulos
print("El circulo 0039")

# Dibuja un circulo azul de radio 10px al centro de la imagen
iMg = cv2.circle(iMg, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen
cv2.imshow("Circulo 0039", iMg)
cv2.waitKey(0)
cv2.destroyAllWindows


# Textos
print("Texto 0039")
# Añade a la imagen el texto "Example Text" en color blanco
iMg = cv2.putText(iMg, "Example Text", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

# Abre la ventana con la imagen
cv2.imshow("Texto 0039", iMg)
cv2.waitKey(0)
cv2.destroyAllWindows


# Thresholding
print("Thresholding 0039")
    
Img = cv2.imread('triple t.jpg',0)

ret,thr1 = cv2.threshold(Img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(Img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(Img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(Img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(Img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()


# Trackbars
print("Trackbars 0039")
def on_trackbar(val):
  print(val)

# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R','frame',0,255,on_trackbar)
cv2.createTrackbar('G','frame',0,255,on_trackbar)
cv2.createTrackbar('B','frame',0,255,on_trackbar)

while(True):
    cv2.imshow('frame',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R','frame')
    g = cv2.getTrackbarPos('G','frame')
    b = cv2.getTrackbarPos('B','frame')

    img[:] = [b,g,r]

cv2.destroyAllWindows()

print("Hecho por Caleb Dorado NC = 0039")