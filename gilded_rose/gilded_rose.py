# -*- coding: utf-8 -*-


class QualityUpdater:
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS_RAGNAROS = "Sulfuras, Hand of Ragnaros"

    @classmethod
    def process(cls, item):
        if item.name == cls.SULFURAS_RAGNAROS:
            return
        elif item.name == cls.AGED_BRIE:
            cls.aged_brie_quality_processor(item)
        elif item.name == cls.BACKSTAGE_PASSES:
            cls.backstage_pasess_quality_processor(item)
        else:
            cls.regular_item_processor(item)

    @staticmethod
    def regular_item_processor(item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = item.quality - 1

    @staticmethod
    def aged_brie_quality_processor(item):
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1

    @staticmethod
    def backstage_pasess_quality_processor(item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1
        if item.sell_in < 6 and item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = item.quality - item.quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            QualityUpdater.process(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
