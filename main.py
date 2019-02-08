from mybox import MyBox

box = MyBox()

box.add(1)
box.add('Two')
box.add(4.5)
box.add('box')
box.add(7)
box.add('Done')


box.remove('Two')
if ('One' in box) and (len(box) > 0):
    box.remove('One')

for i in box:
    print(i)