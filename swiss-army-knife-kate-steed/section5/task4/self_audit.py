import os
import psutil

p = psutil.Process(os.getpid())

start_memory = p.memory_info().rss / (1024 * 1024) # bytes to MB

print(f"--- Starting Footprint ---")
print(f"Memory Usage: {start_memory} MB")

# Generate a large list of numbers
number_gen = [i for i in range(5000000)]

end_memory = p.memory_info().rss / (1024 * 1024)

print(f"--- End Footprint ---")
print(f"Memory Usage: {end_memory} MB")


#Results:

# --- Starting Footprint ---
# Memory Usage: 12.5 MB
# --- End Footprint ---
# Memory Usage: 203.875 MB
