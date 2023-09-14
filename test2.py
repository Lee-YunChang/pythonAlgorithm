import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'topArticles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER limit as parameter.
# base url for copy/paste:
# https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
#


url = "https://jsonmock.hackerrank.com/api/articles?page="
def topArticles(limit):

    data_list = []

    for i in range(limit):

        response = requests.get(url=url + str(i+1))
        data_list.extend(json.loads(response.content.decode('utf-8'))["data"])

    sorted_data_list = sorted(data_list, reverse=True, key=lambda x: x['num_comments'] if x['num_comments'] is not None else 0)

    top_limit_titles = [item['title'] for item in sorted_data_list[:limit]]

    return top_limit_titles


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    limit = int(input().strip())

    result = topArticles(limit)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
