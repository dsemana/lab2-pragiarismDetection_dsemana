#!/usr/bin/env bash

# Setup script for the plagiarism detector project.
# Creates required directories and logs the actions to setup.log.

set -euo pipefail

LOG_FILE="setup.log"

log() {
  local message="$1"
  # Prepend a timestamp to each log entry
  echo "$(date '+%Y-%m-%d %H:%M:%S') - ${message}" | tee -a "${LOG_FILE}"
}

main() {
  log "Starting project setup."

  # Create required directories
  mkdir -p essays
  log "Ensured directory 'essays' exists."

  mkdir -p reports
  log "Ensured directory 'reports' exists."

  log "Setup completed successfully."
}

main "$@"


