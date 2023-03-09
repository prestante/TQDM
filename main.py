import random
from tqdm import tqdm
from time import sleep

print("Demonstration in process ...")
for i in tqdm(range(1000), colour='green'):
    sleep(random.uniform(0.001, 0.01))
print("Demonstration completed")
