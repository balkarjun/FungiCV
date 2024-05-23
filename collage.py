from PIL import Image

paths = [
    './data/defungi/H2/H2_39b_2.jpg', './data/defungi/H6/H6_39a_3.jpg', './data/defungi/H5/H5_104a_2.jpg', './data/defungi/H6/H6_52a_13.jpg', 
    './data/defungi/H3/H3_25a_2.jpg', './data/defungi/H6/H6_56b_2.jpg', './data/defungi/H1/H1_116b_11.jpg' , './data/defungi/H5/H5_36a_4.jpg'
]

size = 250
margin = 2

nrows = 2
ncols = 4

collage_size = (margin + (size + margin)*ncols, margin + (size + margin)*nrows)
collage = Image.new(mode='RGB', size=collage_size)

for i in range(nrows):
    for j in range(ncols):
        idx = i*ncols + j
        image = Image.open(paths[idx])
        image.thumbnail((size, size))

        img_pos = (margin + (size + margin)*j, margin + (size + margin)*i)
        collage.paste(image, box=img_pos)

collage.save('collage.jpg')
