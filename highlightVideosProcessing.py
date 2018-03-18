import numpy
from PIL import Image
import cv2
import pytesseract 
from os import system


from PIL import EpsImagePlugin
#/Users/admin/Library/Python/2.7/lib/python/site-packages/cv2/__init__.py




print(cv2.__version__)
vidcap = cv2.VideoCapture('NAVI vs NEWBEE - CIS vs CHINA ELIMINATION - MAJOR DreamLeague 8 DOTA 2.mp4')
success,image = vidcap.read()
count = 0
success = True
pytesseract.pytesseract.tesseract_cmd  = "/usr/local/Cellar/tesseract/3.05.01/bin/tesseract"
count = 19

file = open("times.txt","w") 


while success:
  success,image = vidcap.read()
  count += 1
  if (count > 20) :
  	count -= 20
  if (count < 20) :
  	continue
  #print 'Read a new frame: ', success
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  #img = cv2.imread("frame"+str(count)+".jpg")
  h, w, a = image.shape
  mid = w / 2
  margin = 50
  crop_img = image[17:25, mid-13:mid+12]
  #print h,w
  #cv2.imshow("Img", image)
  #cv2.imshow("Crop", crop_img)
  cv2.imwrite("crop.jpg", crop_img)

  basewidth = 300
  im = Image.open("crop.jpg")
  wpercent = (basewidth/float(im.size[0]))
  hsize = int((float(im.size[1])*float(wpercent)))
  im = im.resize((basewidth,hsize), Image.ANTIALIAS)
  
  im.save("crop-600.png", dpi=(600,600))
  try:
    results = pytesseract.image_to_string(Image.open('crop-600.png'))
    file.write(results)
    file.write("\n")

  except UnicodeEncodeError:
    a = 0
    #print "Couldn't detect anything"
  
  #cv2.waitKey(0)
  #cv2.imshow("cropped", crop_img)
  if (count>200):
  	break
  count += 1
file.close()