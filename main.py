import time

from fastapi import FastAPI

from src.context.simulation_batch_insert_context import scraper_service as batch_scraper_service
from src.context.simulation_single_insert_context import scraper_service as single_scraper_service

app = FastAPI()


@app.get("/start/single-insert/query-check/{nbr_threads}")
def start(nbr_threads: int):
    single_scraper_service.start(nbr_threads, False)
    return str(nbr_threads) + " threads used.\n" + __stop_simulation()


@app.get("/start/single-insert/index-check/{nbr_threads}")
def start(nbr_threads: int):
    single_scraper_service.start(nbr_threads, True)
    return str(nbr_threads) + " threads used.\n" + __stop_simulation()


@app.get("/start/batch-insert/query-check/{nbr_threads}")
def start(nbr_threads: int):
    batch_scraper_service.start(nbr_threads, False)
    return str(nbr_threads) + " threads used.\n" + __stop_simulation()


@app.get("/start/batch-insert/index-check/{nbr_threads}")
def start(nbr_threads: int):
    batch_scraper_service.start(nbr_threads, True)
    return str(nbr_threads) + " threads used.\n" + __stop_simulation()


@app.get("/stop")
def stop():
    return "Threads stopped\nNbr insertion attempts: " + str(
        single_scraper_service.stop_and_gather_nbr_insertion_attempts())


def __stop_simulation():
    time.sleep(60)
    return stop()
