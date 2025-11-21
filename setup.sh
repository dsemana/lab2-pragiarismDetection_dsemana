#!/usr/bin/env bash

set -euo pipefail

#create the log file
LOG_FILE="setup.log"

#funtion to log messages with timestamps
log() {
  local message="$1"
  echo "$(date '+%Y-%m-%d %H:%M:%S') - ${message}" | tee -a "${LOG_FILE}"
}

#directory setup
main() {
  log "Starting project setup."
  mkdir -p essays
  log "Ensured directory 'essays' exists."

  mkdir -p reports
  log "Ensured directory 'reports' exists."

  log "Setup completed successfully."
}

main "$@"