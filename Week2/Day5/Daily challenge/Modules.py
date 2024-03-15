import requests
import time


def measure_response_time(url):
    start_time = time.time()
    response = requests.get(url)
    elapsed_time = time.time() - start_time
    return elapsed_time


try:
    print(measure_response_time('https://www.google.com/'))
    print(measure_response_time('https://www.youtube.com/'))
    print(measure_response_time('https://www.octopus.developers.institute/courses.com/'))
except:
    pass
