#!/usr/bin/env python3
""" takes two integer arguments and returns a tuple of size two """
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Range of the page

    Args: 
    page: current page
    page_size: Total size of the page

    Return:
    tuple with the start and end

     """
    if page < 1 or page_size < 1:
        return None
    
    start_index: int = (page - 1) * page_size
    end_index: int = (page * page_size)

    return (start_index, end_index)