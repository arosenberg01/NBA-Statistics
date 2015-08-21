import scrapy
from nfl.items import FootballPlayer
import json

class EspnSpider(scrapy.Spider):
    name = 'espn_games_spider'
    allowed_domains = 'espn.com'
    # start_urls = ['http://espn.go.com/nfl/teams']
    # start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/13934/antonio-brown']
    # start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/14874/andrew-luck']
    start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/11307/jamaal-charles']
    # start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/13229/rob-gronkowski']
    # start_urls = ['http://espn.go.com/nfl/player/gamelog/_/id/10452/adrian-peterson']

    stats_table_xpath = '//*[@id="content"]/div[6]/div[1]/div/div[4]/div/table[1]'

    def parse(self, response):
        player_table = []

        for row in response.xpath('//*[@id="content"]/div[6]/div[1]/div/div[4]/div/table[1]/tr'):
            new_row = []
            for col in row.xpath('td/text()'):
                # print('------')
                value = col.extract()
                new_row.append(value)
                # print(col.extract())

            player_table.append(new_row)

        # print(player_table)
        print json.dumps(player_table, indent=1)
        # for table_row in player_table:
        #     for table_column in table_row:
        #         print(table_column)


