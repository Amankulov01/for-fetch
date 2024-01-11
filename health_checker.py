import time
import requests
import yaml

def read_endpoints(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', {})
        )
        return response.status_code >= 200 and response.status_code < 300 and response.elapsed.total_seconds() * 1000 < 500
    except Exception as e:
        return False

def log_availability(availability):
    for domain, stats in availability.items():
        total_requests = stats['total']
        up_requests = stats['up']
        percentage = (up_requests / total_requests) * 100 if total_requests > 0 else 0
        print(f"{domain} has {round(percentage)}% availability")

def main(file_path):
    endpoints = read_endpoints(file_path)

    availability = {}

    try:
        while True:
            for endpoint in endpoints:
                domain = endpoint['url'].split('//')[1].split('/')[0]
                stats = availability.get(domain, {'total': 0, 'up': 0})

                if check_health(endpoint):
                    stats['up'] += 1

                stats['total'] += 1
                availability[domain] = stats

            log_availability(availability)
            time.sleep(15)

    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    file_path = input("Enter the path to the configuration file: ")
    main(file_path)
