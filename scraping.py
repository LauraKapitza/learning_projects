import requests
import re
import random

# VARIABLES
word_to_look_for = "Kim Kardashian"
first_url = "https://en.wikipedia.org/wiki/Special:Random"
# Filter all the href with this string
wiki_link = "/wiki/"
# base url of wikipedia, used to build a new link
wiki_url = 'https://en.wikipedia.org'

# keep track of the amount of time the function was called
count = 1
# limit the amount of time the function can be called
limit = 100

# FUNCTION
# our amazing scraping function
def recursive_search(url, keyword, count, limit):
    # get the content of the url passed
    response = requests.get(url)
    # store the text of the page in the variable
    storage_content = response.text

    # find the h1 in the page and store its content in the variable title
    title = re.findall(r'<h1 id="firstHeading" class="firstHeading" lang="en">(.+?)</h1>',storage_content)[0]

    # check if the keyword is the title
    if keyword in title:
        print(f'{count}. This url contains the keyword in the title: {url}')
    else:
        # gets all the href of the page
        hrefs = re.findall(r'href=[\'"]?([^\'" >]+)', storage_content)
        # create a empty list
        wiki_list = []
        # loop through all of the href links
        for href_content in hrefs:
            # check if the current href start with "wiki_link" (/wiki/)
            if href_content.startswith(wiki_link):
                # if yes, then add it to our new list: wiki_list
                wiki_list.append(href_content)

        # print the amount of href of the current page
        print(f"Amount of href in the current page: {len(wiki_list)}")

        # build a new url from a random href of our list
        next_link = wiki_url + random.choice(wiki_list)
        # Increase our counter and assign it to a new variable
        new_count = count + 1
        # check if our new counter is superior to our given limit
        # Note: superior so that we reach the limit. limit included
        # ex:
        # limit = 5
        # we want to also call the 5th url
        if new_count > limit:
            # yes, return and stop everything
            return
        else:
            # print our new counter and the next link
            print(f'{new_count}. {next_link}')
            # call our function again with the new link
            # the new count and the limit
            # Note: this is the HEART of the recursive function
            recursive_search(next_link, keyword, new_count, limit)


# START
recursive_search(first_url, word_to_look_for, count, limit)