# creating a class with the name Scraping
# defining an __init__ method to initiate first url, keyword and limit
# defining a start method that launch the scraping process
# return the url and count if the keyword is found
# otherwise return a text that said "Nope!"
#

import requests
import re
import random


class Scraping:
    # Filter all the href with this string
    WIKI_LINK = "/wiki/"
    # base url of wikipedia, used to build a new link
    WIKI_URL = 'https://en.wikipedia.org'

    def __init__(self, url, keyword):
        # constructor attributes
        self.url = url
        self.keyword = keyword


        # private attributes
        self.limit = 100
        self.count = 1

        #default value
        self.debug = False

    # method to set the debug attribute
    def set_debug(self, value):
        self.debug = value

    # method to set the debug attribute
    def set_limit(self, value):
        self.limit = value

    def search(self):
        if self.debug == True:
            print("Start searching")
        # Note: count=self.count
        return self.recursive_search(self.url, self.keyword, self.count, self.limit)


    def recursive_search(self, url, keyword, count, limit):
        # get the content of the url passed
        response = requests.get(url)
        # store the text of the page in the variable
        storage_content = response.text

        # find the h1 in the page and store its content in the variable title
        title = re.findall(r'<h1 id="firstHeading" class="firstHeading" lang="en">(.+?)</h1>',storage_content)[0]

        # check if the keyword is the title
        if keyword in title:
            print(f'{count}. This url contains the keyword in the title: {url}')
            return url
        else:
            # gets all the href of the page
            hrefs = re.findall(r'href=[\'"]?([^\'" >]+)', storage_content)
            # create a empty list
            wiki_list = []
            # loop through all of the href links
            for href_content in hrefs:
                # check if the current href start with "wiki_link" (/wiki/)
                if href_content.startswith(Scraping.WIKI_LINK):
                    # if yes, then add it to our new list: wiki_list
                    wiki_list.append(href_content)

            if self.debug == True:
                # print the amount of href of the current page
                print(f"Amount of href in the current page: {len(wiki_list)}")

            # build a new url from a random href of our list
            next_link = Scraping.WIKI_URL + random.choice(wiki_list)
            # Increase our counter and assign it to a new variable
            new_count = count + 1
            # check if our new counter is superior to our given limit
            # Note: superior so that we reach the limit. limit included
            # ex:
            # limit = 5
            # we want to also call the 5th url
            if new_count > limit:
                # yes, return and stop everything
                return "Nope!"
            else:
                if self.debug == True:
                    # print our new counter and the next link
                    print(f'{new_count}. {next_link}')
                # call our function again with the new link
                # the new count and the limit
                # Note: this is the HEART of the recursive function
                return self.recursive_search(next_link, keyword, new_count, limit)




word_to_look_for = "ing"
first_url = "https://en.wikipedia.org/wiki/Special:Random"
super_scraping_variable = Scraping(first_url, word_to_look_for)
super_scraping_variable.set_debug(True)
super_scraping_variable.set_limit(10)
search_response = super_scraping_variable.search()

print(f"Url = {search_response}")
