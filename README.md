# Lyft Bike Share Data

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Tests](https://github.com/williambdean/lyft-bikes/actions/workflows/tests.yml/badge.svg)](https://github.com/williambdean/lyft-bikes/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/lyft-bikes.svg)](https://badge.fury.io/py/lyft-bikes)
[![docs](https://github.com/williambdean/lyft-bikes/actions/workflows/docs.yml/badge.svg)](https://williambdean.github.io/lyft-bikes/)

Python client for Lyft bike share data.

## Features

- Support for [cities](https://www.lyft.com/bikes#cities) with Lyft bike share
- [Historical trips](https://williambdean.github.io/lyft-bikes/examples/historical-trips/)
- Live station and bike / scooter availability
- [Applying pricing to trips](https://williambdean.github.io/lyft-bikes/examples/new-pricing/)
    - Unlock Fees
    - Minute Rates

## Installation

Install from `pip`

```shell
$ pip install lyft-bikes
```

## Documentation

The documentation is hosted on [GitHub Pages](https://williambdean.github.io/lyft-bikes/).

## Development

The development environment was created with [`poetry`](https://python-poetry.org/docs/). The `pyproject.toml` file is the main configuration file for the project.

```bash
poetry install .
```

## Contributing

If you would like to contribute or find some issue in the code, please [open an Issue](https://github.com/williambdean/lyft-bikes/issues/new) or a PR on GitHub. Thanks!
