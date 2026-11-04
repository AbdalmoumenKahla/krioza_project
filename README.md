# Odoo Project

Starter Odoo 18 project with PostgreSQL and a mounted custom addon.

## Requirements

- Docker Desktop with Compose

## Start

```powershell
docker compose up -d
```

Open <http://localhost:8069> and create a database. Use `admin` as the database manager password.

## Custom addon

The starter addon is in `addons/project_base`. After creating the database, enable developer mode, update the Apps list, and install **Project Base**.

## Stop

```powershell
docker compose down
```

To remove persisted databases and Odoo data too:

```powershell
docker compose down -v
```
