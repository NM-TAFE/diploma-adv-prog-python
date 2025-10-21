def read_logs(log_file_path):
    with open(log_file_path, "r") as file:
        for line in file:
            yield line.strip()