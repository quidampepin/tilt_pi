line = subprocess.check_output(cmd, shell=True).decode("utf-8")
data = line.split(',') 

name = data[4]
sg = float(data[3])

# Get temp and convert to C
temp = float(data[2])

# How old is our file? If the data is more than 60 minutes old, print "No Data"
ft = os.stat(fn)
age = (time.time()-ft.st_mtime)
if age > 60*60: 
    status = "No data"
else:
    status = "{:.3f}".format(sg) + " | " + str(temp)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

#draw.text((x, top + 8), str(sg) + " | " + str(temp), font=font, fill=255)
#draw.text((x, top + 8), "{:.3f}".format(sg) + " | " + str(temp), font=font, fill=255)

#font = ImageFont.load_default()
font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/verdana.ttf', 11)
draw.text((x, top + 0), name, font=font, fill=255)

font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/verdana.ttf', 19)
draw.text((x, top + 14), status, font=font, fill=255)

# Display image.
disp.image(image)
disp.show()

# Sleep for a minute
time.sleep(60)



