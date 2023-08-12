from datetime import datetime, date
import json
from pprint import pprint


def parse_competitors(competitors_file_path: str) -> dict:
    with open(competitors_file_path, encoding="utf8") as f:
        return json.load(f)


def parse_results(results_file_path: str) -> list[list]:
    results_list = []
    with open(results_file_path, encoding='utf-8-sig') as f:
        for line in f:
            results_list.append(line.split(' '))
    return results_list


def count_time(start: str, finish: str) -> str:
    start_time = datetime.strptime(start, "%H:%M:%S,%f").time()
    finish_time = datetime.strptime(finish, "%H:%M:%S,%f").time()
    return str(datetime.combine(date.min, finish_time) - datetime.combine(date.min, start_time))


def sum_up_results(competitors: dict, results: list) -> list[list]:
    complex_results = []
    for i in range(0, len(results), 2):
        complex_results.append(
            [
                None,
                results[i][0],
                competitors[results[i][0]]["Surname"],
                competitors[results[i][0]]["Name"],
                count_time(results[i][2][:-1], results[i+1][2][:-1]),
            ]
        )
    complex_results = sorted(complex_results, key=lambda x: x[4])
    for i in range(len(complex_results)):
        complex_results[i][0] = i + 1
    return complex_results


if __name__ == "__main__":
    competitors = parse_competitors("competitors2.json")
    results = parse_results("results_RUN.txt")
    complex_results = sum_up_results(competitors, results)
    header = ["Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"]
    pprint([header, ] + complex_results)
