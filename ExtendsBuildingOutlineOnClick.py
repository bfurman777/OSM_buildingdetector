'''
Written by james on 11/3/2018
Feature: Grabs the outline of a shape a user identifies.

Edited by Brian F on 11/28/2018
Added Rectangle Object and Rectangle Merging
Feature: Computer-detected shapes on click merge as another building is detected from another click

NOTE: image must be in grayscale
'''
#TODO ADD a new_rectangles function


import cv2
import time

# Testing, remove later
filename = 'some_houses_gray.png'   #has to be in same file directory, in greyscale      _gray


image = cv2.imread(filename).copy()
height = image.shape[0]
width = image.shape[1]

# all rectangles are parallel to the xy axis
class Rectangle:
    all_rectangles = []
    removed_rectangles = [] # access removed_rectangles with get_removed_rectangles()
    tolerable_distance_to_combine_rectangles = 21 # arbitrary number
    id = 0

    def __init__(self, init_points):
        self.points = init_points   # a point is a tuple
        self.id = Rectangle.id
        Rectangle.id += 1

        print("")
        print("all_rectangles {}".format(self.arr_all_rect_id()))

        if len(self.points) > 4:
            self.points = self.points[:4]
            print('TOO MANY POINTS IN A RECTANGLE')

        Rectangle.all_rectangles.append(self)
        print("Adding {} to all_rectangles".format(self.get_id_str()))
        print("all_rectangles {}".format(self.arr_all_rect_id()))

        # try to merge with all other rectangles, but if close enough
        for i in range(0, len(Rectangle.all_rectangles) - 1):
            if Rectangle.all_rectangles[i].merge_with(self):
                break
        self.draw_all()

    # temp for debugging
    def arr_all_rect_id(self):
        id_arr = []
        for rect in Rectangle.all_rectangles:
            id_arr.append(rect.get_id_str())
        return id_arr

    def merge_with(self, other_rectangle):

        for point in other_rectangle.points:
            # if the rectangles overlap
            if self.has_point_inside_approx(point):
                # get cords for the merged rectangle
                top = min(self.get_up_bound(), other_rectangle.get_up_bound())
                bot = max(self.get_down_bound(), other_rectangle.get_down_bound())
                right = max(self.get_right_bound(), other_rectangle.get_right_bound())
                left = min(self.get_left_bound(), other_rectangle.get_left_bound())

                # remove the old components of the new merged rectangle

                print("merging {} and {}".format(self.get_id_str(), other_rectangle.get_id_str()))

                Rectangle.removed_rectangles.append(other_rectangle)
                Rectangle.removed_rectangles.append(self)

                Rectangle.all_rectangles.remove(other_rectangle)
                Rectangle.all_rectangles.remove(self)

                Rectangle([(right, top), (left, top), (left, bot), (right, bot)])

                return True
        return False

    # Checks if a point is inside/on the borders
    def has_point_inside(self, point_to_check):
        has_up_bound, has_down_bound, has_left_bound, has_right_bound = False, False, False, False
        # check all lines in this rectangle, does the point lay in between 4 lines
        for i in range(0, len(self.points)):
            point1 = self.points[i]
            point2 = self.points[(i+1) % len(self.points)]
            # if vertical line
            if point1[0] == point2[0]:
                if point1[1] < point_to_check[1] < point2[1] or point1[1] > point_to_check[1] > point2[1]:
                    # point_to_check is within the y-range of the line
                    if point_to_check[0] >= point1[0]:
                        has_left_bound = True
                    if point_to_check[0] <= point1[0]:
                        has_right_bound = True
            # if horizontal line
            if point1[1] == point2[1]:
                if point1[0] < point_to_check[0] < point2[0] or point1[0] > point_to_check[0] > point2[0]:
                    # point_to_check is within the x-domain of the line
                    if point_to_check[1] >= point1[1]:
                        has_down_bound = True
                    if point_to_check[1] <= point1[1]:
                        has_up_bound = True
        return has_up_bound and has_down_bound and has_left_bound and has_right_bound

    # check if point is close enough to be inside
    def has_point_inside_approx(self, point_to_check, tolerable_distance = tolerable_distance_to_combine_rectangles):
        slide_right = self.has_point_inside((point_to_check[0] + tolerable_distance, point_to_check[1]))
        slide_left = self.has_point_inside((point_to_check[0] - tolerable_distance, point_to_check[1]))
        slide_up = self.has_point_inside((point_to_check[0], point_to_check[1] - tolerable_distance))
        slide_down = self.has_point_inside((point_to_check[0], point_to_check[1] + tolerable_distance))
        return slide_right or slide_left or slide_up or slide_down

    # returns leftmost x cord
    def get_left_bound(self):
        left_bound = self.points[0][0]
        for point in self.points:
            if point[0] < left_bound:
                left_bound = point[0]
        return left_bound

    # returns rightmost x cord
    def get_right_bound(self):
        right_bound = self.points[0][0]
        for point in self.points:
            if point[0] > right_bound:
                right_bound = point[0]
        return right_bound

    # returns smallest y cord
    def get_up_bound(self):
        up_bound = self.points[0][1]
        for point in self.points:
            if point[1] < up_bound:
                up_bound = point[1]
        return up_bound

    # returns largest y cord
    def get_down_bound(self):
        down_bound = self.points[0][1]
        for point in self.points:
            if point[1] > down_bound:
                down_bound = point[1]
        return down_bound

    # once you get the removed rectangles, the removed rectangles is cleared
    @staticmethod
    def get_removed_rectangles():
        temp = Rectangle.removed_rectangles.copy()
        Rectangle.removed_rectangles.clear()
        return temp

    @staticmethod
    def get_all_rectangles():
        return Rectangle.all_rectangles

    def get_id(self):
        return self.id

    # just for debugging
    def get_id_str(self):
        return "id{}".format(self.get_id())

    @staticmethod
    def draw_all():
        for rect in Rectangle.all_rectangles:
            for i in range(0, len(rect.points)):
                cv2.line(image, rect.points[i], rect.points[(i + 1) % len(rect.points)], (255, 0, 0), 5)
            # print(rect.points)
        # print('')


def draw_left(x, y, threshold, timeout):
    """
    Draws the line to the left
    :param x: X coordinate of click
    :param y: Y coordinate of click
    :param threshold: pixel gradient threshold
    :param timeout: timeout (sec)
    :return: X coordinate where pixel gradient is hit
    """
    x_position = x
    while x_position != 1:
        x_position -= 1
        if time.time() > timeout:
            break

        # Setting the value of the compare image
        if x_position < 10:
            left_x_compare = 0
        else:
            left_x_compare = x_position - 10

        # Getting intensities
        current_intensity = int(image[y, x_position, 0])  # the current intensity of pixel
        compare_intensity = int(image[y, left_x_compare, 0])  # intensity of pixel you want to compare

        if abs(current_intensity - compare_intensity) > threshold:
            return left_x_compare
    return 0



def draw_up(x, y, threshold, timeout):
    """
    Draws the line up
    :param x: X coordinate of click
    :param y: Y coordinate of click
    :param threshold: pixel gradient threshold
    :param timeout: timeout (sec)
    :return: Y coordinate where pixel gradient is hit
    """
    y_position = y
    while y_position != 1:
        y_position -= 1
        if time.time() > timeout:
            break

        # Setting the value of the compare image
        if y_position < 10:
            up_y_compare = 0
        else:
            up_y_compare = y_position - 10

        # Getting intensities
        current_intensity = int(image[y_position, x, 0])  # the current intensity of pixel
        compare_intensity = int(image[up_y_compare, x, 0])  # intensity of pixel you want to compare

        if abs(current_intensity - compare_intensity) > threshold:
            return up_y_compare
    return 0


def draw_down(x, y, threshold, timeout):
    """
    Draws the line down.
    :param x: X coordinate of click
    :param y: Y coordinate of click
    :param threshold: pixel gradient threshold
    :param timeout: timeout (sec)
    :return: Y coordinate where pixel gradient is hit
    """
    y_position = y
    while y_position != height - 1:
        y_position += 1
        if time.time() > timeout:
            break

        # Setting the value of the compare image
        if y_position > height - 11:
            down_y_compare = height - 11
        else:
            down_y_compare = y_position + 10

        # Getting intensities
        current_intensity = int(image[y_position, x, 0])  # the current intensity of pixel
        compare_intensity = int(image[down_y_compare, x, 0])  # intensity of pixel you want to compare

        if abs(current_intensity - compare_intensity) > threshold:
            return down_y_compare
    return height


def draw_right(x, y, threshold, timeout):
    """
    Draws the line to the right
    :param x: X coordinate of click
    :param y: Y coordinate of click
    :param threshold: pixel gradient threshold
    :param timeout: timeout (sec)
    :return: X coordinate where pixel gradient is hit
    """
    x_position = x
    while x_position != width - 1:
        x_position += 1
        if time.time() > timeout:
            break

        # Setting the value of the compare image
        if x_position > width - 11:
            right_x_compare = width - 11
        else:
            right_x_compare = x_position + 10

        # Getting intensities
        current_intensity = int(image[y, x_position, 0])  # the current intensity of pixel
        compare_intensity = int(image[y, right_x_compare, 0])  # intensity of pixel you want to compare

        if abs(current_intensity - compare_intensity) > threshold:
            return right_x_compare
    return width


# GETS USER CLICKS
def getMouse(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        threshold = 50
        timeout = time.time() + 5  # 5 seconds to timeout
        top = draw_up(x, y, threshold, timeout)
        bot = draw_down(x, y, threshold, timeout)
        right = draw_right(x, y, threshold, timeout)
        left = draw_left(x, y, threshold, timeout)

        # TODO there is an error when bad cords are given by the draw_(direction) functions (at the edge, giving 'None')
        # fix by changing the return cords on the draw_(direction) functions
        # temp fix:
        #if top is None or bot is None or right is None or left is None:
         #   return

        Rectangle([(right, top), (left, top), (left, bot), (right, bot)])

    if event == cv2.EVENT_RBUTTONDOWN:
        print('PRINT ALL RECTS TO UPDATE')
        for rect in Rectangle.get_removed_rectangles():
            print(rect.points)
        print('END THE PRINTING\n')


# bind the function to window
cv2.namedWindow('DrawOutline')
cv2.setMouseCallback('DrawOutline', getMouse)

# Do until esc pressed
while 1:
    # TODO FIND BETTER WAY TO REDRAW
    # redraws all buildings every frame, but shouldn't matter too much because the user sees only 1 pic at a time
    # clears the image
    image = cv2.imread(filename).copy()
    Rectangle.draw_all()
    cv2.imshow('DrawOutline', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
# if esc pressed, finish.
cv2.destroyAllWindows()
