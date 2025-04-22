# BLAKE3 Hash Benchmark (Dockerized)

This project provides a lightweight, containerized benchmark tool for measuring the maximum BLAKE3 hashing throughput using parallel CPU workers. Designed for performance profiling on ARM-based systems like the Orange Pi 5 Plus, as well as general-purpose Linux systems.

---

## Features

- Fixed input string hashed repeatedly using the BLAKE3 algorithm
- Fully configurable via environment variables
- Parallel execution using multiple processes
- Controlled benchmark duration
- Results saved with timestamp in the `/results` directory
- Lightweight and portable Docker container

---

## Configuration via Environment Variables

| Variable             | Description                                | Example         |
|----------------------|--------------------------------------------|-----------------|
| `CONCURRENT_WORKERS` | Number of parallel worker processes         | `4`             |
| `SECONDS_TO_RUN`     | Duration of the benchmark in seconds        | `10`            |
| `FIXED_STRING`       | Input string to hash repeatedly             | `HelloWorld`    |

---

### Build the Docker Image

```bash
docker build -t blake3-benchmark .
```

## Docker Run Usage
You need the following files
```
DockerFile
hash_benchmark.py
```
Then you need to build the image manually
```
docker build -t blake3-benchmark .
```

Run the container (it will delete it selfe after the run is done)

```
docker run --rm \
  -e CONCURRENT_WORKERS=4 \
  -e SECONDS_TO_RUN=10 \
  -e FIXED_STRING=HelloWorld \
  -v $(pwd)/results:/results \
  blake3-benchmark
```

Testing multiple workers
```
for w in 4 6 8 10 12; do
  docker run --rm -e CONCURRENT_WORKERS=$w -e SECONDS_TO_RUN=10 -v $(pwd)/results:/results blake3-benchmark
done
```

## Docker Compose Usage
```
docker compose up 
```

## TODO
I will shortly provie an image that can be used from the docker hub. So you don't need to build your own image

## Performance Tests
### Orange Pi5 Plus (32GB RAM)




