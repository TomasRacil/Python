import base64

## FF D8 == SOI
## FF D9 == EOI
## message = base64_bytes.decode('ascii')


def jpencode(infile, message, outfile):
    
    if (outfile[-4] != ".jpg"):
	    outfile + ".jpg"

    message_bytes = message.encode('ascii')
    message = base64.b64encode(message_bytes)
    
    original_image = infile.read()
    output = open(outfile, "w+b")
    output.write(original_image)
    PlaceAtEoi(output)
    output.write(message)
    output.close()

def jpdecode(infile):
    PlaceAtEoi(infile)
    message_bytes = infile.read()
    message = base64.b64decode(message_bytes)
    text = message.decode('ascii')
    print("\nThe text is: " + text)


    

def PlaceAtEoi(infile):
    infile.seek(0, 0)
    while(1):
        byte = infile.read(1)
        if (byte == ''):
            printf("\nEOF ERROR! Is this really JPEG?")
            exit()
        if (byte == (b'\xFF')):
            byte = infile.read(1)
            if (byte == (b'\xD9')):
                return    

