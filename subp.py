import subprocess



process = subprocess.run(['bentoml --version'],check=True,stdout=subprocess.PIPE,universal_newlines=True)

output = process.stdout

print(output)
