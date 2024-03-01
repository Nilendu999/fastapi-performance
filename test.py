import cv2
import numpy as np
font_scale = 2
font_thickness = 4
color_fill= (135,206,250)

def create_circle(image, x1, y1, x2, y2):
    print(f"'circle' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    radius_x = abs(x2 - x1) // 2
    radius_y = abs(y2 - y1) // 2

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    cv2.ellipse(image, (center_x, center_y), (radius_x, radius_y), 0, 0, 360, color_fill, thickness=-1)
    # Add text in the middle of the circle
    text = "Circle"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = center_x - text_size[0] // 2
    text_y = center_y + text_size[1] // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

def create_rectangle(image, x1, y1, x2, y2):
    print(f"'rectangle' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    cv2.rectangle(image, (x1, y1), (x2, y2),color_fill, thickness=-1)
    # Add text in the middle of the rectangle
    text = "Rectangle"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (x1 + x2) // 2 - text_size[0] // 2
    text_y = (y1 + y2) // 2 + text_size[1] // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

def create_parallelogram(image, x1, y1, x2, y2):
    print(f"'parallelogram' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    width = abs(x2 - x1)
    side = 0.25 * width  # Length of sides parallel to x-axis is 0.75 times the width in x

    # Ensure the parallelogram fits inside the bounding box defined by x1, x2, y1, y2
    top_left_x = x1+side  # Left x-coordinate
    top_left_y = y1  # Top y-coordinate

    top_right_x = x2  # Right x-coordinate
    top_right_y = y1  # Top y-coordinate

    bottom_left_x = x1  # Left x-coordinate
    bottom_left_y = y2  # Bottom y-coordinate

    bottom_right_x = x2-side  # Right x-coordinate
    bottom_right_y = y2  # Bottom y-coordinate

    pts = np.array([[top_left_x, top_left_y], [top_right_x, top_right_y], [bottom_right_x, bottom_right_y], [bottom_left_x, bottom_left_y]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(image, [pts], color_fill)
    # Add text in the middle of the parallelogram
    text = "Parallelogram"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = int((top_left_x + top_right_x) // 2 - text_size[0] // 2)
    text_y = int((top_left_y + bottom_left_y) // 2 + text_size[1] // 2)
    cv2.putText(image, text, (text_x, text_y), font, font_scale*0.8, (0, 0, 0), font_thickness)

def create_rhombus(image, x1, y1, x2, y2):
    print(f"'rhombus' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    pts = np.array([[x1, (y1 + y2) // 2], [(x1 + x2) // 2, y1], [x2, (y1 + y2) // 2], [(x1 + x2) // 2, y2]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(image, [pts], color_fill)
    # Add text in the middle of the rhombus
    text = "Rhombus"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (x1 + x2) // 2 - text_size[0] // 2
    text_y = (y1 + y2) // 2 + text_size[1] // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

def create_triangle(image, x1, y1, x2, y2):
    print(f"'triangle' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    pts = np.array([[x1, y2], [(x1 + x2) // 2, y1], [x2, y2]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(image, [pts], color_fill)
    # Add text in the middle of the triangle
    text = "Triangle"
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (x1 + x2) // 2 - text_size[0] // 2
    text_y = (y1 + y2) // 2 + text_size[1] // 2
    cv2.putText(image, text, (int(text_x*1.04), text_y), font, font_scale*0.8, (0, 0, 0), font_thickness)

def draw_parallel_line(image, value, orientation):
    if orientation == 'y':
        cv2.line(image, (0, value), (image.shape[1], value), (0, 0, 0), thickness=1)
    elif orientation == 'x':
        cv2.line(image, (value, 0), (value, image.shape[0]), (0, 0, 0), thickness=1)

def create_line(image, x1, y1, x2, y2):
    print(f"'line' : [{int(x1/10)},{int(y1/10)},{int(x2/10)},{int(y2/10)}]")
    cv2.line(image, (x1, y1), (x2, y2), (0,0, 255), thickness=3)
    # Add text in the middle of the line
    # text = "Line"
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # font_scale = 0.5
    # font_thickness = 1
    # text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    # text_x = (x1 + x2) // 2 - text_size[0] // 2
    # text_y = (y1 + y2) // 2 + text_size[1] // 2
    # cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

def save_image(image, filename):
    cv2.imwrite(filename, image)

background = np.ones((3100, 1350 , 3), dtype=np.uint8) * 255

spacing = 20
x=350
y=50
# Draw shapes on the image with anti-aliasing and spacing
create_circle(background, 450-x, 50-y, 950-x, 550-y)
create_line(background,700-x,550-y,700-x,850-y)
create_rhombus(background, 400-x, 850-y, 1000-x, 1450-y)
create_line(background,700-x,1450-y,700-x,1750-y)
create_parallelogram(background,400-x,1750-y,1000-x,2050-y)
create_line(background,700-x,2050-y,700-x,2350-y)
create_rectangle(background,350-x,2350-y,1050-x,2650-y)
create_line(background,1050-x,2500-y,1350-x,2500-y)
create_line(background,700-x,2650-y,700-x,2950-y)
create_triangle(background,1200-x,2350-y,1700-x,2650-y)
create_line(background,1450-x,2650-y,1450-x,3050-y)
create_circle(background,350-x,2950-y,1050-x,3150-y)
create_line(background,1050-x,3050-y,1450-x,3050-y)

dict_reduced_values = {'circle' : [10,0,60,50], 'line1' : [35,50,35,80], 'rhombus' : [5,80,65,140], 'line2' : [35,140,35,170], 'parallelogram' : [5,170,65,200], 'line3' : [35,200,35,230], 'rectangle' : [0,230,70,260], 'line4' : [70,245,100,245], 'triangle' : [85,230,135,260], 'line5' : [35,260,35,290], 'line6' : [110,260,110,300], 'line7' : [70,300,110,300], 'oval' : [0,290,70,310]}
# create_triangle(background, 260, 20, 300, 40)
# create_line(background, 320, 30, 360, 10)

# draw_parallel_line(background, 450, 'x')
# draw_parallel_line(background, 50, 'y')
# draw_parallel_line(background, 950, 'x')
# draw_parallel_line(background, 550, 'y')

# Save the image with all shapes
save_image(background, "shapes_image.jpg")
