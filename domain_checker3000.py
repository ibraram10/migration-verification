import requests
import csv


class fileReader:
    def __init__(self, file_path, column_name):
        self.file_path = file_path
        self.column_name = column_name

    def read_csv(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row[self.column_name] for row in reader]
        

class domainChecker:
    def __init__(self, data):
        self.data = data

    def is_domain_reachable(self, domain):
        try:
            response = requests.get(f'http://{domain}', timeout=5)
            # if the response status code is 200, the domain is reachable
            return response.status_code == 200
        except requests.RequestException:
            return False

    def check_domains(self):
        unreachable_domains = []
        for domain in self.data:
            if not self.is_domain_reachable(domain):
                unreachable_domains.append(domain)
        return unreachable_domains