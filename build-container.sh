# Script to build container

export BASEREG=quay.io/wcaban
export DTAG=$(date +%y%m%d%H%M)
export BUILD_AND_UPLOAD=True

podman build -t ${BASEREG}/mockup-mec -f containers/Containerfile .

if [ "$BUILD_AND_UPLOAD" == "True" ]; then
    podman tag      ${BASEREG}/mockup-mec:latest ${BASEREG}/mockup-mec:${DTAG}
    podman push     ${BASEREG}/mockup-mec:latest
    podman push     ${BASEREG}/mockup-mec:${DTAG}
fi