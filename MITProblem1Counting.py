#!/usr/bin/env python
# MIT by Vitali

order = raw_input().split()
def item_order(order):
    newOrder = order.split()
    hamburger = []
    salad = []
    water = []
    for i in newOrder:
        if i == 'hamburger':
            hamburger.append(i)
        if i == 'salad':
            salad.append(i)
        if i == 'water':
            water.append(i)
#def item_order(order):
    result = "salad:%s hamburger:%s water:%s" % (str(len(salad)),str(len(hamburger)),str(len(water)))
    return result
