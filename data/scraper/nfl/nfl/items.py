# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Player(Item):
    name = Field()
    number = Field()
    team = Field()
    position = Field()
    stats = Field()

class Game_Log(Item):
    header = Field()
    columns = Field()
    reg_season_totals = Field()
    reg_season_games = Field()