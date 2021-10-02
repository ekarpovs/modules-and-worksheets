'''
QR code operations
Uses https://github.com/lincolnloop/python-qrcode
'''
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *

# from qrcode import constants

def create(params, **data):
  '''
  Creates qr code.

  parameters:
    - params:
      --n;r;[1,40,1];3-- version: size of QR code (smallest - 21*21 pix)
      --n;r;[1,20,1];2-- box-size: number of pix for each block of QR code
      --n;r;[4,10,1];4-- border: thickness of the boder of the boxes
      --n;d;[L:1,M:0,Q:3,H:2];M-- error-level: error correction level, qrcode.constants.ERROR_CORRECT_(...)
      --str;s;[];Some data-- qr-data: QR code data - string
      --b;f;[False,True];True-- fit: best fit for the data to avoid data overflow errors
      --n;d;[BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6];BLACK-- fcolor: QR code fill color
      --n;d;[BLACK:0,WHITE:1,RED:2,GREEN:3, BLUE:4,MAGENTA:5,CYAN:6];WHITE-- bcolor: QR code background color
      --n;d;[SQUARE:0,ROUND:1,CIRCLE:2,VERTICA:3,HORIZONTAL:4];SQUARE-- drower: shape of QR code blocks
      --n;d;[SOLID:0,RADIAL:1,SQUARE:2,HORIZONTAL:3,VERTICAL:4,IMAGE:5];SOLID-- gradient: gradient or embedded image
    - data: 
      image - reference to an source image
  returns:
    - data:
      - image: QR code.
  '''
  version = params.get('version', 3)
  box_size = params.get('box-size', 2)
  border = params.get('border', 4)
  error_correction = params.get('error-level', qrcode.constants.ERROR_CORRECT_M) 
  qr_data = params.get('qr-data', 'Some data')
  fit = params.get('fit', True)
  fill_color = params.get('fcolor', 0)
  back_color = params.get('bcolor', 1)
  drower = params.get('drower', 0)
  gradient = params.get('gradient', 0)
  qr = qrcode.QRCode(
      version=version,
      error_correction=error_correction,
      box_size=box_size,
      border=border,
  )
  qr.add_data(qr_data)
  qr.make(fit=fit)

  colors = ['black', 'white', 'red', 'green', 'blue', 'magenta', 'cyan']
  drowers = [SquareModuleDrawer, RoundedModuleDrawer, CircleModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer]
  masks = [
    SolidFillColorMask,
    RadialGradiantColorMask, 
    SquareGradiantColorMask, 
    HorizontalGradiantColorMask, 
    VerticalGradiantColorMask,
    ImageColorMask 
    ]

  factory = StyledPilImage
  module_drower = drowers[drower] 
  color_mask = masks[gradient]

  qr_img_pil = qr.make_image(
    back_color=colors[back_color], 
    fill_color=colors[fill_color], 
    image_factory=factory,
    module_drawer=module_drower(), 
    color_mask=color_mask()
    )
  # qr_img_pil = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
  # qr_img_pil = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")  # qr_img_pil = qr.make_image(back_color=colors[back_color], fill_color=colors[fill_color], image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
  # qr_img_pil = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
  data['image-pil'] = qr_img_pil
  data['image'] = qr_img_pil
  # data['image'] = qr_img_pil
  return data