import json

def write_name(name):
    with open("./files/names.txt", 'a') as f:
        f.write(name+'\n')


def read_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def find_obj(key, value, json_content):
    for obj in json_content:
        if obj[key] == value:
           return obj

    return None


def endpoint_increment_total_request(url, method):

    with open("../files/endpoints_data.json", 'r+') as f:
        json_data = json.loads(f.read())
        obj = find_obj('url', url, json_data)
        obj["stats"]["total_requests_received"] += 1
        f.write(json.dumps(json_data))


def endpoint_avg_handling_time(url, time):

    with open("../files/endpoints_data.json", 'r+') as f:
        json_data = json.loads(f.read())
        obj = find_obj('url', url, json_data)
        obj["stats"]["avg_handling_time"] = time


def update_summary_json():

    data = read_file_content('endpoints_data.json')
    data = json.loads(data)

    summary_json = read_file_content('summary.json')
    summary_json = json.loads(summary_json)

    for obj in data:
        if obj["stats"]["total_requests_received"] > summary_json["highest_requests"]["number"]:
            summary_json["highest_requests"]["number"] = {"name" : obj["stats"]}