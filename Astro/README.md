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

## Add Dag
- Setup dependencies
```shell
python3 -m venv .venv
source .venv/Scripts/activate
pip3 install airflow
pip3 install airflow-operators

```

## Check Dag

- Some old Airflow concepts are completely removed and dags are not detected if they are used
- Fix by running
```shell
 astro dev upgrade-test

```

- I had to change `schedule_interval` to `schedule` for dag to be discovered
