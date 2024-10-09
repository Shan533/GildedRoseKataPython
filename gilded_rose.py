# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

class ItemUpdater:
    """Base class for item updater."""
    def __init__(self, item):
        self.item = item

    def update(self):
        pass

class NormalItemUpdater(ItemUpdater):
    """Updater for normal items."""
    def update(self):
        self.item.sell_in -= 1
        degrade = 1
        if self.item.sell_in < 0:
            degrade *= 2
        self.item.quality = max(0, self.item.quality - degrade)

class AgedBrieUpdater(ItemUpdater):
    """Updater for Aged Brie."""
    def update(self):
        self.item.sell_in -= 1
        increase = 1
        if self.item.sell_in < 0:
            increase *= 2
        self.item.quality = min(50, self.item.quality + increase)

class BackstagePassesUpdater(ItemUpdater):
    """Updater for Backstage passes."""
    def update(self):
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sell_in < 10:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)

class SulfurasUpdater(ItemUpdater):
    """Updater for Sulfuras (legendary item)."""
    def update(self):
        # Sulfuras does not change
        pass

class ConjuredItemUpdater(ItemUpdater):
    """Updater for Conjured items."""
    def update(self):
        self.item.sell_in -= 1
        degrade = 2
        if self.item.sell_in < 0:
            degrade *= 2
        self.item.quality = max(0, self.item.quality - degrade)

class GildedRose:
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update()

    def get_updater(self, item):
        """Factory method to get the appropriate updater for an item."""
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesUpdater(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater(item)
        elif item.name.startswith("Conjured"):
            return ConjuredItemUpdater(item)
        else:
            return NormalItemUpdater(item)
