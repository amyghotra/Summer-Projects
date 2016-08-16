from PIL import Image

userInputImage = input("Choose an image to alter .jpg.")
im = Image.open(userInputImage)
data = list(im.getdata())					   #gets the the RGB values of each pixel

def addTuples(tuple):
	return tuple[0] + tuple[1] + tuple[2] 		

red = (140, 35, 24)
blue = (94, 140, 106)
green = (136, 166, 94)
yellow = (242, 196, 98)
palette1=[red, blue, green, yellow]

dark_red = (61, 0, 12)
passion_fruit = (169, 10, 42)
sky_blue = (89, 183, 167)
off_white = (251, 254, 211)
palette2 = [dark_red, passion_fruit, sky_blue, off_white]

teal = (1, 9, 76)
light_green = (177, 212, 154)
yellow = (227, 198, 98)
orange = (250, 149, 35)
purple = (62, 30, 33)
palette3 = [teal, light_green, yellow, orange, purple]

newpixels = []									#list of RGB values

user_input= input("palette1 or palette2 or palette3")		#user chooses palette colors

def filter(palette):							#what comes up when a certain palette is chosen
		for i in data:
			sum = addTuples(i)
			if sum < 182:						#the 182= the intensity of certain part of picture
				newpixels.append(palette[0])  	#if intensity = less than 182 = color number "0" on list  
			elif sum <364:
				newpixels.append(palette[1])
			elif sum <546:
				newpixels.append(palette[2])
			elif sum >= 546:
				newpixels.append(palette[3])


if user_input == "palette1":
	filter(palette1)
if user_input == "palette2":
	filter(palette2)
if user_input == "palette3":
	filter(palette3)


new_image = Image.new(im.mode, im.size)
new_image.putdata(newpixels)
new_image.save("output.jpg", "jpeg")


#thank you Brad M. for having such a helpful Intro to PIL blog <3 <3