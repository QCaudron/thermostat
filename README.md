# Instructions

Identify the disk of your SD card.
```
diskutil list
```

Unmount the SD card.
```
diskutil unmountDisk /dev/<disk_id>
```

Copy the disk image to the SD card.
```
sudo dd bs=1m if=image.img of=/dev/r<disk_id> conv=sync
```

Create an empty file called `ssh` in the boot partition.
```
df -h
cd /Volumes/boot
touch ssh
```

Remember to ssh into the Raspberry Pi for the first time after install in order to add it to known_hosts.


