# files-docker

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Docker](https://www.docker.com/).

Files:
- [`Dockerfile`](./bundle/Dockerfile)
- [`.dockerignore`](./bundle/.dockerignore)

```sh
# Add Docker files to your Meltano project
meltano add files docker
```

By default, your Meltano project's Docker image is built from the [`meltano/meltano:latest`](https://hub.docker.com/r/meltano/meltano/tags)
base image which comes with Python 3.6 and the latest version of Meltano.
If you'd like to use a different image (e.g. `your-company/meltano:latest`) or a specific version (e.g. `meltano/meltano:v1.37.0`),
you can override the `MELTANO_IMAGE` [`--build-arg`](https://docs.docker.com/engine/reference/commandline/build/#set-build-time-variables---build-arg).

```sh
# Build image using latest Meltano version
docker build --tag demo-project:dev .

# Build image using Meltano version 1.37.0
docker build \
  --tag demo-project:dev \
  --build-arg MELTANO_IMAGE=meltano/meltano:v1.37.0 \
  .
```

Since the built image's [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint)
will be [the `meltano` command](https://meltano.com/docs/command-line-interface.html),
you can provide `meltano` subcommands and arguments directly to
[`docker run <image-name> ...`](https://docs.docker.com/engine/reference/commandline/run/)
as trailing arguments.

```sh
# View Meltano version
docker run demo-project:dev --version

# List scheduled pipelines
docker run demo-project:dev schedule list
```
