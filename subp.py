import subprocess



process = subprocess.run(['bentoml'],check=True,stdout=subprocess.PIPE,universal_newlines=True)

output = process.stdout

print(output)
