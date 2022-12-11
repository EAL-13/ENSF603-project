from fastapi import FastAPI

from src.context.simulation_batch_insert_context import scraper_service as batch_scraper_service
from src.context.simulation_single_insert_context import scraper_service as single_scraper_service

app = FastAPI()


@app.get("/start/single-insert/query-check/{nbr_threads}")
def start(nbr_threads: int):
    single_scraper_service.start(nbr_threads, False)
    return str(nbr_threads) + " threads started"


@app.get("/start/single-insert/index-check/{nbr_threads}")
def start(nbr_threads: int):
    single_scraper_service.start(nbr_threads, True)
    return str(nbr_threads) + " threads started"


@app.get("/start/batch-insert/query-check/{nbr_threads}")
def start(nbr_threads: int):
    batch_scraper_service.start(nbr_threads, False)
    return str(nbr_threads) + " threads started"


@app.get("/start/batch-insert/index-check/{nbr_threads}")
def start(nbr_threads: int):
    batch_scraper_service.start(nbr_threads, True)
    return str(nbr_threads) + " threads started"


@app.get("/stop")
def stop():
    single_scraper_service.stop()
    return "Threads stopped"
