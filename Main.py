from jinja2 import Template

participants = []
mock = 'mock/index.html'
image_path = r'https://storage.yandexcloud.net/studvesnafma2/img/'
devider = "<span class=\"spacer\"></span><br/><span class=\"spacer\"></span>"
devider_br = "<br><span class=\"spacer\"></span><br/><span class=\"spacer\"></span>"
reward_level = {'0': '',
                '1': 'лауреат I степени',
                '2': 'лауреат II степени',
                '3': 'лауреат III степени',
                '4': 'Гран-При'}

colors = {'red': (212, 47, 47),
          'blue': (47, 121, 212),
          'green': (33, 194, 81),
          'orange': (255, 171, 25)}

placeholder = {'left bot': 0,
               'left top': 1,
               'right top': 2,
               'right bot': 3}


def read_file():
    f = open('list.txt', 'r', encoding='utf-8')
    global participants
    for line in f:
        names, nomination, sub, medal, color, place, img = line.split(';')
        if img[-1] == '\n':
            img = img[:-1]
        participants.append([names.split(','), nomination, sub,medal, color,placeholder.get(place),  img])
    f.close()


read_file()
counter = 0
for participant in participants:

    counter += 1
    print(counter, participant)
    names = participant[0]
    nomination = participant[1] + devider + participant[2]
    image_file = image_path + str(participant[6]) + '.jpg'
    h = Template(open(mock, encoding='utf-8').read())
    f = open('renders/{}.html'.format('{}'.format(counter)), 'w', encoding='utf-8')
    f.write(h.render(names=names, second=nomination, third=reward_level.get(participant[3]), img_url=image_file,
                     place=participant[5], color=colors.get(participant[4])))
    f.close()
