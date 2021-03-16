import click

import cloudscraper
import time
from rich.table import Table
from rich.console import Console

@click.command()
@click.option('--minimum', help="Minimum tulip price to show", default=0)
@click.option('--threshold', help="Threshold where the price is green", default=300)
@click.option('--watch', help="Whether or not to watch for the islands constantly", is_flag=True)
def turnips(minimum, threshold, watch):
    scraper = cloudscraper.create_scraper()
    console = Console()        
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Name", style="dim")
    table.add_column("Price")
    table.add_column("Description")
    table.add_column("URL")
    req = scraper.post('https://api.turnip.exchange/islands/')
    test = req.json()
    prices = [[
                island['turnipPrice'],
                island['turnipPrice'].__str__(),
                island['name'],
                island['description'],
                'https://turnip.exchange/island/'+island['turnipCode']
            ] for island in test['islands'] if island['turnipPrice'] > minimum]
    prices.sort(key=lambda x:x[0], reverse=True)
    for price in prices:
        table.add_row("[bold green]"+price[1]+"[/bold green]" if price[0] > threshold else "[bold red]"+price[1]+"[/bold red]", 
                        *price[2:])
    console.print(table)
    if watch:
        time.sleep(10)
    while watch:
        table = Table(show_header=True, header_style="bold green")
        table.add_column("Name", style="dim")
        table.add_column("Price")
        table.add_column("Description")
        table.add_column("URL")
        req = scraper.post('https://api.turnip.exchange/islands/')
        test = req.json()
        prices = [[
                    island['turnipPrice'],
                    island['turnipPrice'].__str__(),
                    island['name'],
                    island['description'],
                    'https://turnip.exchange/island/'+island['turnipCode']
                ] for island in test['islands'] if island['turnipPrice'] > minimum]
        prices.sort(key=lambda x:x[0], reverse=True)
        for price in prices:
            table.add_row("[bold green]"+price[1]+"[/bold green]" if price[0] > threshold else "[bold red]"+price[1]+"[/bold red]", 
                            *price[2:])
        console.clear()
        console.print(table)
        time.sleep(10)