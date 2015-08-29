import scrapy
import json
from scrapy.utils.response import get_base_url
from urlparse import urljoin

class EspnSpider(scrapy.Spider):
    name = 'espn_game_stats'
    allowed_domains = ['espn.com', 'espn.go.com']
    start_urls = ['http://espn.go.com/nfl/teams']

    # Follows all links to nfl teams' depth charts
    def parse(self, response):
        base_url = get_base_url(response)

        depth_charts = response.xpath('//a[text()="Depth Chart"]/@href').extract()
        for depth_chart in depth_charts:
            link = urljoin(base_url, depth_chart)
            yield scrapy.http.Request(link, callback = self.parse_depth_chart)

    # Follows all links for individual QBs, WRs, TEs, RBs, and FBs on team depth chart
    def parse_depth_chart(self, response):

        rows = response.xpath('//*[@id="my-teams-table"]/div[4]/div[1]/table/tr')
        for row in rows:
            players = row.xpath('td/strong/a | td/a')
            # players = row.xpath('td//a')

            names = players.xpath('text()').extract()
            links = players.xpath('@href').extract()
            cols = row.xpath('td')
            position = cols[0].xpath('text()').extract()[0]

            if position == 'QB' or position == 'WR' or position == 'TE' or position == 'RB' or position == 'FB':
                if len(links) > 0:
                    for link, name in zip(links, names):
                        yield scrapy.http.Request(link, callback = self.go_to_game_log)

    # Follows link to player's game long for most recent year
    # TODO: add argument for year?
    def go_to_game_log(self, response):
        game_log = response.xpath('//*[@id="content"]/div[6]/div[1]/div[2]/div/p/a/@href').extract()

        if game_log:
            game_log = game_log[0]
            print('\n')
            base_url = get_base_url(response)
            absolute_path = urljoin(base_url, game_log)
            print('going to game log', absolute_path)
            yield scrapy.http.Request(absolute_path, callback = self.parse_game_log)

    # Convert stats table into array of arrays
    # TODO: parse headers and regular season totals
    def parse_game_log(self, response):
        games_table = []

        rows = response.xpath('//*[@id="content"]/div[6]/div[1]/div/div[4]/div/table[1]/tr')

        for row in rows:

            game_row = []
            for col in row.xpath('td'):

                opponent = col.xpath('ul/li[3]/a/text()').extract()
                game_result = col.xpath('a/text()').extract()
                other_value = col.xpath('text()').extract()

                if opponent:
                    game_row.append(opponent[0])
                elif game_result:
                    game_row.append(game_result[0])
                else:
                    game_row.append(other_value[0])

            games_table.append(game_row)

        print json.dumps(games_table, indent=1)








