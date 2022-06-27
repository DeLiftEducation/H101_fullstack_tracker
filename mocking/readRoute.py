import json


def read(file_path):
    with open(file_path, encoding='utf8') as f:
        data = json.load(f)
        return data

def get_segments(file_path):
    all_data = read(file_path)
    segments = all_data["segments"]
    return segments
