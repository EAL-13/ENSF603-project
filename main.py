from fastapi import FastAPI
from src.context.simulation_context import scraper_service

scraper_service.start(2)
scraper_service.stop()
app = FastAPI()


@app.get("/start/{nbr_threads}")
def start(nbr_threads: int):
    scraper_service.start(nbr_threads)
    return str(nbr_threads)+" threads started"


@app.get("/stop")
def stop():
    scraper_service.stop()
    return "Threads stopped"
