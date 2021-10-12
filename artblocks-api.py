import requests
import json

project_number = 37
project_feature = "Type"
project_value = "Swarm"
starting_token = 0


def get_token_count(project_number):
    project_url = "https://api.artblocks.io/project/" + str(project_number)
    project_response = requests.request("GET", project_url)
    for line in project_response.text.split("<p>"):
        if "Maximum Invocations: " in line:
            invocations = line.split("Maximum Invocations: ")[1]
            result = invocations.split("<")[0]
            return result


def get_token_features(token, id, feature):

    token_url = "https://token.artblocks.io/" + str(id)

    token_response = requests.request("GET", token_url)

    if token_response.status_code == 200:
        features = json.loads(token_response.text)["features"]
    else:
        return "SKIPPED"

    if feature:
        if features[project_feature] == project_value:
            return token
    else:
        results = {}
        results[str(id)] = features


def send_it(token_count):

    if not project_feature:
        results = {}
        feature = False
    else:
        results = []
        feature = True

    token = starting_token

    while token < token_count:

        if token < 10:
            fill = "00000"
        elif token < 100:
            fill = "0000"
        elif token < 1000:
            fill = "000"
        elif token < 10000:
            fill = "00"

        id = str(project_number) + fill + str(token)

        result = get_token_features(token, id, feature)
        if result == "SKIPPED":
            print("SKIPPED " + id)
        elif result:
            results.append(result)
            print(results)

        if token % 10 == 0:
            print(str(token) + "/" + str(token_count))
        token += 1

    return results


token_count = get_token_count(project_number)

try:
    results = send_it(int(token_count))
    print(results)
except KeyboardInterrupt:
    print("ya stopped it, aye")
