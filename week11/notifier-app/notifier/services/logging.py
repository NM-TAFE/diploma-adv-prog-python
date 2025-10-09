import logging

def action_logger(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        logging.info(f"[ACTION] {user.name} ({user.role()}) is performing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper