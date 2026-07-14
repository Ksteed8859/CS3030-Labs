import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(message)s]",
    filename="app.log",
    filemode="w"

)

logging.info("Script Started")
logging.warning("Low disk space")
logging.error("Database connection failed")