#! /bin/bash

# Test picoweb on ESP8266

CDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

BUILD="${CDIR}/build/esp"
PROJECTS='/vlab/projects'
ESP32_PORT="$PROJECTS/marxworld/electronics/environments/micropython/ports/esp32"
MODUL_DIR=$CDIR/build/tmp/esp-modules

export ESPIDF=/vlab/projects/marxworld/electronics/environments/esp32/esp-idf



mkdir -p $MODUL_DIR

pushd $ESP32_PORT
cp -Lr modules/* $MODUL_DIR/
cp -rf ${CDIR}/src/modules/python/* $MODUL_DIR
# rm -f $MODUL_DIR/neopixel*
# rm -f $MODUL_DIR/webrep*
# rm -f $MODUL_DIR/webs*
rm -f $MODUL_DIR/ds18*




make clean BUILD=${BUILD}

if make -j8 BUILD=${BUILD} FROZEN_MPY_DIR=$MODUL_DIR
then
    echo Build Finished
else
    echo Build Failed
fi

# esptool.py  --port /dev/ttyUSB0 erase_flash

# if make -j 8 FROZEN_MPY_DIR=$DIRECTORY
# then
#     sleep 1
#     esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect -fm dio 0 build/firmware-combined.bin
#     sleep 4
#     rshell -p /dev/ttyUSB0 --buffer-size=30 --editor nano
# else
#     echo Build failure
# fi

popd