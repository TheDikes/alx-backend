#!/usr/bin/env python3
""" takes two integer arguments and returns a tuple of size two """

def index_range(page: int, page_size: int):
    """
    Range of the page

    Args: 
    page: current page
    page_size: Total size of the page

    Return:
    tuple with the start and end

     """  
    start_index = (page - 1) * page_size
    end_index = (page * page_size)

    return (start_index, end_index)