import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filenamecsv", type = str)
parser.add_argument("filenamexml", type = str)
args = parser.parse_args()

readfile = pd.read_csv('C:\\Users\\givalent\\Desktop\\python\\csv2excel\\'+ args.filenamecsv)

readfile.to_excel('C:\\Users\\givalent\\Desktop\\python\\csv2excel\\' + args.filenamexml, index=None, header=True, sheet_name='Constancias')