def camel_to_snake(name):
    snake = ''
    letters = []
    for i in range(len(name)):
        letters.append(name[i])
        if letters[i].isupper():
            if i == 0:
                snake +=  name[0].lower()
            elif i != 0:
                snake += '%s%s' %('_',name[i].lower())
        elif letters[i].islower() or letters[i].isalpha() == False:
            snake += '%s' % (name[i])

    return snake


def snake_to_camel(name):
    snake = name.split('_')
    camel = ''
    for element in snake:
        camel = camel + element.title()

    return camel


