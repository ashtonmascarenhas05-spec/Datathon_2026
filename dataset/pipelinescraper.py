import csv
import numpy as np
import pandas as pd

class Scraper:

    def __init__(self,csv_file):
        self.csv_file = csv_file

        with open(self.csv,"r")