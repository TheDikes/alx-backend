#!/usr/bin/env python3

""" A function that takes two integer arguments `page` and `page_size`
and returns a tuple of size two """

def index_range(page, page_size):
    if page < 1 or page_size < 1:
        return None
    
    start_index = (page - 1) * page_size
    end_index = (page * page_size)

    return (start_index, end_index)