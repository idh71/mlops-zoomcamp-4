import os

filename = "results.parquet"

# Get the size of the file in bytes
file_size = os.path.getsize(filename)

# Convert bytes to kilobytes
kb_size = file_size / 1024

# Convert bytes to megabytes
mb_size = file_size / (1024 * 1024)

# Convert bytes to gigabytes
gb_size = file_size / (1024 * 1024 * 1024)

# Print the file size in various measurements
print(f"File Size: {file_size} bytes")
print(f"File Size: {kb_size:.2f} KB")
print(f"File Size: {mb_size:.2f} MB")
print(f"File Size: {gb_size:.2f} GB")
