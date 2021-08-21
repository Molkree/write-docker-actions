import requests
import time

# Make an HTTP GET request to the cat-fact API
cat_url = "https://catfact.ninja/fact"
r = requests.get(cat_url)
random_fact = r.json()["fact"]

# Print the individual randomly returned cat-fact
print(random_fact)

sleep_time = 5
time.sleep(sleep_time)

print(f"I've just slept for {sleep_time}")

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
