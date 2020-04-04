#!/usr/bin/env python
# coding: utf-8

import json
import click

@click.command()
@click.option('--jsonfile')
@click.option('--extractpaths')
def reagent(jsonfile: str, extractpaths:str):
    paths = [x.split(":") for x in extractpaths.split(',')]
    
    with open(jsonfile, "r") as thefile:
        num = 0
        for line in thefile:
            output = ""
            try:
                num += 1
                thetweet = json.loads(line)
                for path in paths:
                    item = thetweet
                    for label in path:
                        item = item[label]

                    output += "{}\t".format(str(item).replace("\n"," "))
            except (KeyError, IndexError):
                print("Key missing on line {}.".format(num))
            else:
                print(output)

if __name__ == "__main__":
    reagent()
