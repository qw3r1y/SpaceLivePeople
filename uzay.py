import requests
import json

answer = requests.get("http://api.open-notify.org/astros.json")
people_in_space= answer.json()["number"]

print (f"Number of people in space right now {people_in_space}")


print("NAMES AND TASKS")

print("--------------------")

for people in answer.json()["people"]:
    print(people["name"] , " ------------>   ",people["craft"])