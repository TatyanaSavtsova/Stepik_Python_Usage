import os
import os.path

for current_dir in os.walk("C:/Users/Tatsiana.Sautsova/Downloads/sample"):
    for files in current_dir:
        if files.endswith(".py"):
            print(current_dir)