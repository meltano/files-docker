# files-docker

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [Docker](https://www.docker.com/).

Files:
- [`Dockerfile`](./bundle/Dockerfile)
- [`.dockerignore`](./bundle/.dockerignore)

```sh
# Add Docker files to your Meltano project
meltano add files docker
```

By default, your Meltano project's Docker image is built from the [`meltano/meltano:latest`](https://hub.docker.com/r/meltano/meltano/tags) base image which comes with the latest version of Meltano, and the oldest version of Python supported by Meltano, currently 3.7.

If you'd like to use a different image (e.g. [registry.gitlab.com/meltano/meltano:latest](https://gitlab.com/groups/meltano/-/container_registries/189256?orderBy=NAME&sort=asc&search[]=latest&search[]=) in GitLab Registry, or `your-company/meltano:latest`), a specific version of Meltano (e.g. `meltano/meltano:v1.55.0`), or Python 3.8 or 3.9 (e.g. `meltano/meltano:latest-python3.8` or `meltano/meltano:v1.55.0-python3.9`),
you can modify the `Dockerfile` or override the `MELTANO_IMAGE` [`--build-arg`](https://docs.docker.com/engine/reference/commandline/build/#set-build-time-variables---build-arg).

```sh
# Build image using latest Meltano version
docker build --tag meltano-demo-project:dev .

# Build image using Meltano version 1.55.0 and Python 3.8
docker build \
  --tag meltano-demo-project:dev \
  --build-arg MELTANO_IMAGE=meltano/meltano:v1.55.0-python3.8 \
  .
```

Since the built image's [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint)
will be [the `meltano` command](https://meltano.com/docs/command-line-interface.html),
you can provide `meltano` subcommands and arguments directly to
[`docker run <image-name> ...`](https://docs.docker.com/engine/reference/commandline/run/)
as trailing arguments.

```sh
# View Meltano version
docker run meltano-demo-project:dev --version

# List scheduled pipelines
docker run meltano-demo-project:dev schedule list
```
