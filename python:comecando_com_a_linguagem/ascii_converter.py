import ascii_magic

# my_art = ascii_magic.from_image_file('~/Pictures/nepal.png')
# ascii_magic.to_terminal(my_art)
output = ascii_magic.from_image_file("nixoscolorful.png", columns=60, char="4")
ascii_magic.to_terminal(output)
