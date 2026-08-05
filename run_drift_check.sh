#!/bin/bash

cd /home/youcef/Desktop/network-automation-toolkit
source venv/bin/activate 2>/dev/null

LOGFILE="logs/drift_$(date +%Y%m%d_%H%M%S).log"
mkdir -p logs

python3 check_drift.py >> "$LOGFILE" 2>&1

echo "Drift check completed at $(date)" >> "$LOGFILE"