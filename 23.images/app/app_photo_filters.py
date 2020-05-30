# стоит обязательно попробовать фильтр с предсказанием праздника :)
import argparse, sys
import logging
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

logging.basicConfig(filename='app_photo_filter.log', filemode='w', format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def holiday_predict(img_input):
    holidays = ['Polar Bear Plunge Day', 'Run It up the Flagpole and See If Anyone Salutes It Day',
                'Cut Your Energy Costs Day', 'Soup Swap Day',
                'Popcorn Day', 'Data Privacy Day',
                'Lame Duck Day', 'Carrot Cake Day',
                'Toothache Day', 'Darwin Day',
                'DNA Day', 'Pack Rat Day',
                'Pizza Party Day', 'Chocolate Chip Day',
                'Dance Like a Chicken Day', 'Frog Jumping Day',
                'National Doughnut Day', 'Hug Your Cat Day',
                'Leave the Office Early Day', 'Sauntering Day',
                'International Picnic Day', 'International Panic Day',
                'Camera Day', 'Video Games Day',
                'Yellow Pig Day', 'Girlfriend s Day',
                'Fresh Breath Day', 'Checkers Day',
                'Hobbit Day', 'I Love Lucy Day',
                'Fast Food Day', 'Make Up Your Mind Day',
                'Bicarbonate of Soda Day', 'Card Playing Day',
                'Eggnog Day', 'Ugly Sweater Day',
                'Handbag Day', 'World Smile Day',
                'Sweetest Day', 'Caps Lock Day',
                'Internet Day', 'Magic Day',
                'Zero Tasking Day', 'Saxophone Day',
                'International Stout Day', 'Men Make Dinner Day',
                'Cake Day', 'Computer Security Day',
                'Eat a Red Apple Day', 'Day of the Ninja',
                'Microwave Oven Day', 'Monkey Day',
                'Chic Spy Day', 'Taco Day',
                'Hug Your Hound Day', 'Collect Rocks Day',
                'Guacamole Day', 'National CleanUp Day',
                'National Gymnastics Day', 'International Talk Like a Pirate Day']
    holiday = random.choice(holidays)

    # load image
    img = cv2.imread(img_input)
    logger.debug('[holiday_predict] loading image')

    # detect face
    face_cascade = cv2.CascadeClassifier(
        'lbpcascade_frontalface.xml')
    faces_detected = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    logger.debug('detect face')
    (x, y, w, h) = faces_detected[0]
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
    
    cv2.imwrite('face2.jpg', rect[y + 1:y + h, x + 1:x + w])

    # open images
    logger.debug('[holiday_predict] opening images')
    im1 = Image.open('holiday.jpg')
    im2 = Image.open('face2.jpg')

    # make mask for image
    x, y = im2.size
    eX, eY = x - 35, y - 35
    bbox = (x / 2 - eX / 2, y / 2 - eY / 2, x / 2 + eX / 2, y / 2 + eY / 2)
    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse(bbox, fill=255)
    mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(20))
    logger.debug('[holiday_predict] making mask')
    mask_im_blur.save('mask_circle_blur2.jpg', quality=95)

    # add face
    back_im = im1.copy()
    back_im.paste(im2.resize((118, 117)), (140, 150), mask_im_blur.resize((118, 117)))

    # add text
    logger.debug('[holiday_predict] adding text')
    draw = ImageDraw.Draw(back_im)
    font1 = ImageFont.truetype('ChelseaMarket-Regular.ttf', size=25)
    font2 = ImageFont.truetype('ChelseaMarket-Regular.ttf', size=13)
    (x, y) = (5, 50)
    color1 = 'rgb(154, 0, 0)'
    color2 = 'rgb(103, 2, 114)'
    draw.text((x, y), 'Now you are celebrating', fill=color1, font=font1)
    name = holiday
    (x, y) = (5, 80)
    draw.text((x, y), name, fill=color2, font=font2)

    # save
    logger.debug('[holiday_predict] saving image')
    back_im.save('holiday_im.jpg', quality=95)


def simpson_chalkboard(img_input):
    """ imagine that you Bart who writes phrases in the chalkboard
    """
    # generate random phrase
    chalkboard_phrases = ['I WILL NOT WASTE CHALK', 'I WILL NOT SKATEBOARD IN THE HALLS',
                          'I WILL NOT BURP IN CLASS', 'I WILL NOT INSTIGATE REVOLUTION',
                          'I WILL NOT DRAW NAKED LADIES IN CLASS', 'I DID NOT SEE ELVIS',
                          'I WILL NOT CALL MY TEACHER "HOT CAKES"', 'GARLIC GUM IS NOT FUNNY',
                          'THEY ARE LAUGHING AT ME, NOT WITH ME', 'I WILL NOT YELL "FIRE" IN A CROWDED CLASSROOM',
                          'I WILL NOT ENCOURAGE OTHERS TO FLY', 'I WILL NOT FAKE MY WAY THROUGH LIFE',
                          'TAR IS NOT A PLAYTHING', 'I WILL NOT XEROX MY BUTT',
                          'IT IS POTATO, NOT POTATOE', 'I WILL NOT TRADE PANTS WITH OTHERS',
                          'I AM NOT A THIRTY TWO YEAR OLD WOMAN', 'I WILL NOT DO THAT THING WITH MY TONGUE',
                          'I WILL NOT DRIVE THE PRINCIPAL S CAR', 'I WILL NOT PLEDGE ALLEGIANCE TO BART',
                          'I WILL NOT SELL SCHOOL PROPERTY', 'I WILL NOT CUT CORNERS',
                          'I WILL NOT GET VERY FAR WITH THIS ATTITUDE', 'NOBODY LIKES SUNBURN SLAPPERS',
                          'SPITWADS ARE NOT FREE SPEECH', 'HIGH EXPLOSIVES AND SCHOOL DO NOT MIX',
                          'I WILL NOT BRIBE PRINCIPAL SKINNER', 'BART BUCKS, ARE NOT LEGAL TENDER',
                          'I WILL NOT FAKE RABIES', 'UNDERWEAR SHOULD BE WORN ON THE INSIDE',
                          'THE CHRISTMAS PAGEANT DOES NOT STINK', 'I WILL NOT TORMENT THE EMOTIONALLY FRAIL',
                          'I WILL NOT CARVE GODS', 'I WILL NOT AIM FOR THE HEAD',
                          'I WILL NOT BARF UNLESS I AM SICK', 'I WILL NOT EXPOSE THE IGNORANCE OF THE FACULTY',
                          'I WILL NOT SPIN THE TURTLE', 'I WILL NOT FAKE SEIZURES',
                          'I WILL NOT DISSECT THINGS UNLESS INSTRUCTED', 'I WILL NOT SEND LARD THROUGH THE MAIL',
                          'BAGMAN, IS NOT A LEGITIMATE CAREER CHOICE',
                          'CURSIVE WRITING DOES NOT MEAN WHAT I THINK IT DOES',
                          'I WILL NOT HANG DONUTS ON MY PERSON', 'I WILL NOT STRUT AROUND LIKE I OWN THE PLACE',
                          'THE GOOD HUMOR MAN CAN ONLY BE PUSHED SO FAR',
                          'I DO NOT HAVE POWER OF ATTORNEY OVER FIRST GRADERS',
                          'NERVE GAS IS NOT A TOY', 'I WILL NOT MOCK MRS. DUMBFACE',
                          'THE FIRST AMENDMENT DOES NOT COVER BURPING', 'THIS IS NOT A CLUE...OR IS IT?',
                          'BEWITCHED, DOES NOT PROMOTE SATANISM', 'THE BOYS ROOM IS NOT A WATER PARK',
                          'I WILL STOP TALKING ABOUT THE TWELVE INCH PIANIST', 'I AM NOT CERTIFIED TO REMOVE ASBESTOS',
                          'I DID NOT LEARN EVERYTHING I NEED TO KNOW IN KINDERGARTEN', 'I AM NOT MY LONG-LOST TWIN',
                          'I WILL NOT BE A SNICKERPUSS', 'THE TRUTH IS NOT OUT THERE',
                          'I NO LONGER WANT MY MTV', 'EVERYONE IS TIRED OF THAT RICHARD GERE STORY',
                          'I DID NOT INVENT IRISH DANCING', 'I WILL NOT TEASE FATTY',
                          'BUTT.COM IS NOT MY E-MAIL ADDRESS', 'NO ONE CARES WHAT MY DEFINITION OF "IS" IS',
                          'MY MOM IS NOT DATING JERRY SEINFELD', 'THE PRESIDENT DID IT, IS NOT AN EXCUSE',
                          'NO ONE WANTS TO HEAR ABOUT MY SCIATICA', 'HILLBILLIES ARE PEOPLE TOO',
                          'GRAMMAR IS NOT A TIME OF WASTE', 'IT DOES NOT SUCK TO BE YOU',
                          'I CANNOT ABSOLVE SINS', 'A TRAINED APE COULD NOT TEACH GYM',
                          'I HAVE NEITHER BEEN THERE NOR DONE THAT', 'I AM SO VERY TIRED',
                          'FRIDAYS ARE NOT "PANTS OPTIONAL"', 'PORK IS NOT A VERB',
                          'NON-FLAMMABLE, IS NOT A CHALLENGE', 'I WAS NOT TOUCHED "THERE" BY AN ANGEL',
                          'I AM NOT HERE ON A FARTBALL SCHOLARSHIP', 'DODGEBALL STOPS AT THE GYM DOOR',
                          'A BELCH IS NOT AN ORAL REPORT', 'MY SUSPENSION WAS NOT "MUTUAL"',
                          ]
    chalkboard = random.choice(chalkboard_phrases)

    # load image
    logger.debug('[simpson_chalkboard] loading image')
    img = cv2.imread(img_input)

    # detect face
    face_cascade = cv2.CascadeClassifier(
        'lbpcascade_frontalface.xml')
    faces_detected = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    (x, y, w, h) = faces_detected[0]
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.imwrite('face.jpg', rect[y + 1:y + h, x + 1:x + w])

    # open images
    logger.debug('[simpson_chalkboard] open images')
    im1 = Image.open('bart.jpg')
    im2 = Image.open('face.jpg')

    # make mask for image
    x, y = im2.size
    eX, eY = x - 15, y - 15
    bbox = (x / 2 - eX / 2, y / 2 - eY / 2, x / 2 + eX / 2, y / 2 + eY / 2)
    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse(bbox, fill=255)
    logger.debug('[simpson_chalkboard] making mask')
    mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
    mask_im_blur.save('mask_circle_blur.jpg', quality=95)

    # add face
    back_im = im1.copy()
    back_im.paste(im2.resize((68, 67)), (540, 158), mask_im_blur.resize((68, 67)))

    # add text
    draw = ImageDraw.Draw(back_im)
    font = ImageFont.truetype('Berton-Roman-trial.ttf', size=20)
    (x, y) = (19, 50)
    name = chalkboard
    color = 'rgb(255, 255, 255)'  # white color
    draw.text((x, y), name, fill=color, font=font)
    (x, y) = (19, 70)
    draw.text((x, y), name, fill=color, font=font)

    # save
    logger.debug('[simpson_chalkboard] saving image')
    back_im.save('simpson_chalkboard.jpg', quality=95)

def image_grey(img_input):
    logger.debug('[image_grey] loading image')
    image = Image.open(img_input)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))
    del draw
    logger.debug('[image_grey] saving image')
    image.save('grey.jpg')

def image_neg(img_input):
    logger.debug('[image_neg] loading image')
    image = Image.open(img_input)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    del draw
    logger.debug('[image_neg] saving image')
    image.save('neg.jpg')

def all_filters(img_input):
    image_neg(img_input)
    image_grey(img_input)
    simpson_chalkboard(img_input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Great Application for photo filtering')
    parser.add_argument("-i", "--input", required=True, dest='input')

    funcs = {'holiday_predict': holiday_predict, 'simpson_chalkboard': simpson_chalkboard, 'image_grey': image_grey,
             'image_neg': image_neg,
             'all_filters': all_filters}
    parser.add_argument('-f', '--func', dest='func',
                        choices=['holiday_predict', 'simpson_chalkboard', 'image_grey', 'image_neg', 'all_filters'],
                        required=True,
                        help="""Choose one of the specified function to be run.""")
    args = parser.parse_args()

    # Resolve the chosen function object using its name:
    chosen_func = funcs[args.func]
    chosen_func(args.input)
