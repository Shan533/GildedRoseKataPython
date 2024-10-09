# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                # Legendary item, do nothing
                continue
            else:
                # Decrease sell_in
                item.sell_in -= 1

                if item.name == "Aged Brie":
                    # Increase quality
                    item.quality += 1
                    if item.sell_in < 0:
                        item.quality += 1
                    if item.quality > 50:
                        item.quality = 50
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in < 5:
                        item.quality += 3
                    elif item.sell_in < 10:
                        item.quality += 2
                    else:
                        item.quality += 1
                    if item.quality > 50:
                        item.quality = 50
                elif item.name.startswith("Conjured"):
                    # Decrease quality by 2
                    degrade = 2
                    if item.sell_in < 0:
                        degrade *= 2
                    item.quality -= degrade
                    if item.quality < 0:
                        item.quality = 0
                else:
                    # Normal item
                    degrade = 1
                    if item.sell_in < 0:
                        degrade *= 2
                    item.quality -= degrade
                    if item.quality < 0:
                        item.quality = 0