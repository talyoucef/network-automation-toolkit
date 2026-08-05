# Network Automation Toolkit

Python/Netmiko-based toolkit for automated network configuration backup and drift detection, built and tested against a virtualized FRRouting lab in GNS3.

## What it does

- Connects to a network device over SSH using Netmiko
- Backs up the running configuration with a timestamp
- Compares the live configuration against a saved baseline to detect unauthorized or unexpected changes
- Runs automatically on a schedule via cron, logging results

## Architecture

```text
[Your PC]
    |
    | SSH
    v
[FRR Router (GNS3/Docker)]
    |
    +--> backup_config.py ---> backups/
    |
    +--> check_drift.py -----> baseline_config.txt
    |                          |
    |                          +--> logs/
    |
    +--> run_drift_check.sh (cron)
```

## How to run it

1. Set up a `.env` file with `FRR_HOST`, `FRR_USER`, `FRR_PASSWORD`.
2. `pip install -r requirements.txt`
3. `python3 backup_config.py`
4. `python3 check_drift.py`
5. `./run_drift_check.sh`
6. Optionally schedule via cron:

```bash
0 * * * * /path/to/run_drift_check.sh
```

## Example output

```diff
DRIFT DETECTED:
--- baseline
+++ current
@@ -8,6 +8,7 @@
 no ipv6 forwarding

 ip route 0.0.0.0/0 192.168.122.1
+ip route 10.0.0.0/24 192.168.122.1

 interface eth0
 ip address 192.168.122.10/24
```

## What I'd add with more time

- Support for multiple devices instead of just one
- Alerting (email/Slack) when drift is detected instead of just logging
- Automatic rollback to the baseline configuration
