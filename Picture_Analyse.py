from Read_Image import Read_Image_Feature


filename = 'Test/T-10.jpeg'

XY = Read_Image_Feature(filename)

x_test = XY[0]
y_test = XY[1]

print(x_test, ",", y_test)