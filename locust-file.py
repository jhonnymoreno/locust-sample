
import time
import random
from locust import HttpUser, task, between

class DemoUser(HttpUser):
    wait_time = between(1,3)

    @task
    def city_info(self):
        self.client.get("/ma/belmont", name="/city-info")

    @task(3)
    def zip_code_info(self):
        zip_code = random.randrange(23401,23800)
        self.client.get(f"/{zip_code}", name="/zip-info")
        time.sleep(5)
    
    def on_start(self):
        ...