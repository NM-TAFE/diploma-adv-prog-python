import logging

logging.basicConfig(format="[%(levelname)s] %(asctime)s - %(message)s",
                    level=logging.DEBUG,
                    )

print("I am here")
logging.info("I am here")
logging.debug(f"I am {__name__=} also here debugging")
logging.error("OH OH - Error")
logging.warning("WATCH OUT")
raf_log = logging.getLogger(__name__)
raf_log.info("Wrote to a log")
raf_log2 = logging.getLogger(__name__)
print(raf_log is raf_log2)

