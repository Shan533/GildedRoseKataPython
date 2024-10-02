# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
    
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
    
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)  # Expected quality after degrading by 2
        self.assertEqual(2, items[0].sell_in)
    
    def test_quality_never_negative_after_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", -1, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(gilded_rose.items[0])
        self.assertGreaterEqual(gilded_rose.items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
