# Script to build container
export BASEREG=quay.io/wcaban
export DTAG=$(date +%y%m%d)

podman build -t ${BASEREG}/mockup-mec -f containers/Containerfile .
# podman tag      ${BASEREG}/mockup-mec:latest ${BASEREG}/mockup-mec:${DTAG}
# podman push     ${BASEREG}/mockup-mec:latest
# podman push     ${BASEREG}/mockup-mec:${DTAG}