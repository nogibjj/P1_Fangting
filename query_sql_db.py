#!/usr/bin/env python

import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT name, est_diameter_min, hazardous FROM neo_v2_csv ORDER BY est_diameter_min LIMIT 5",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)


# run the CLI
if __name__ == "__main__":
    cli()
