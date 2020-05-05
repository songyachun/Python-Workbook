# -*-coding=utf-8-*-
'''
# @Author         : SYACHUN
# @Date           : 2020-04-07 10:47:30
# @LastEditTime: 2020-04-18 21:27:12
# @LastEditors: SYACHUN
# @FilePath       : \Python-Workbook\Data Structures and Algorithms\Chaper 4 递归\4-2标尺.py
# @Description    : 
'''


from pysnooper import snoop
# @snoop()


def draw_line(tick_length, tick_label=''):
    """ Draw one line with given tick lengh (followed by optional label). """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

# @snoop()


def draw_interval(center_length):
    """ Draw tick interval based upon a central tick length. """
    if center_length > 0:
        draw_interval(center_length-1)
        draw_line(center_length)
        draw_interval(center_length-1)

# @snoop()


def draw_rule(num_inches, major_length):
    """ Draw English ruler with given number of inches,major tick length """
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))


if __name__ == "__main__":
    draw_rule(20, 5)
