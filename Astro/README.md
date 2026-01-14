# Airflow with Astro

- [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli)
- [Astro Cloud](https://www.astronomer.io/)

## Initialize Dev Project

```shell
astro dev init
```

## Start Project

- [Run Airflow Locally](https://www.astronomer.io/docs/astro/cli/run-airflow-locally)
- Update global config 

```shell
cp global/config.yaml ~/.astro/config.yaml
```

I had to change below items

```yaml
api-server:
  port: "38080"
postgres:
  host: host.docker.internal
webserver:
  port: "38080"

```

```shell
asttro dev start
```

