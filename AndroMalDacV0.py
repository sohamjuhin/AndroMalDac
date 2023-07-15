import os
import hashlib

def scan_apk(apk_path):
    try:
        with open(apk_path, 'rb') as file:
            content = file.read()
            apk_hash = hashlib.sha256(content).hexdigest()
            print(f"Scanning: {apk_path}")
            print(f"APK Hash: {apk_hash}")
            # Perform additional static analysis on the APK file
            # Add your own malware detection logic here
            print("Scan complete. No malware detected.\n")
    except IOError:
        print(f"Error scanning: {apk_path}\n")

def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".apk"):
                apk_path = os.path.join(root, file)
                scan_apk(apk_path)

if __name__ == "__main__":
    target_directory = "/path/to/directory"  # Replace with the target directory containing APK files
    scan_directory(target_directory)
