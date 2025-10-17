# TWRP Device Tree for Realme 11 Pro 5G (RMX3771)

## Device Specifications

| Feature | Specification |
|---------|---------------|
| Device | Realme 11 Pro 5G |
| Codename | RMX3771 |
| Manufacturer | Realme |
| Chipset | MediaTek Dimensity 7050 (6nm) |
| CPU | Octa-core (2x2.6 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55) |
| GPU | Mali-G68 MC4 |
| Memory | 8GB / 12GB RAM |
| Storage | 128GB / 256GB |
| Battery | 5000 mAh, 67W SUPERVOOC |
| Display | 6.7" AMOLED, 1080 x 2412 pixels, 120Hz |
| Camera | 100MP (main) + 2MP (depth) |
| Android Version | Android 13, Realme UI 5.0 |
| Architecture | ARM64 |

## Features

- [x] Boot into TWRP
- [x] ADB
- [x] Decrypt /data (FBE)
- [x] Display
- [x] Touch
- [x] Vibration
- [x] Backup/Restore
- [x] Flash ZIP files
- [x] MTP
- [x] USB OTG
- [x] Brightness control
- [x] Mount system partitions

## Building TWRP

### Prerequisites

You need a Linux environment (Ubuntu 20.04+ recommended) to build TWRP:

```bash
# Install required packages
sudo apt-get update
sudo apt-get install -y bc bison build-essential ccache curl flex \
    g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev \
    lib32readline-dev lib32z1-dev liblz4-tool libncurses5 libncurses5-dev \
    libsdl1.2-dev libssl-dev libxml2 libxml2-utils lzop pngcrush rsync \
    schedtool squashfs-tools xsltproc zip zlib1g-dev python-is-python3 \
    openjdk-11-jdk android-tools-adb android-tools-fastboot
```

### Install repo tool

```bash
mkdir -p ~/bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
export PATH=~/bin:$PATH
```

### Initialize TWRP Minimal Manifest

```bash
mkdir -p ~/twrp
cd ~/twrp

# Initialize TWRP 12.1 manifest
repo init -u https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp.git -b twrp-12.1

# Sync the repositories (this will take time and bandwidth)
repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags
```

### Add Device Tree

```bash
# Clone this device tree
git clone https://github.com/YOUR_USERNAME/android_device_realme_RMX3771 device/realme/RMX3771

# Or manually copy the device tree folder to:
# ~/twrp/device/realme/RMX3771
```

### Build TWRP

```bash
cd ~/twrp

# Set up environment
source build/envsetup.sh

# Choose your device
lunch twrp_RMX3771-eng

# Build recovery image
mka recoveryimage -j$(nproc --all)
```

### Build Output

After successful build, you'll find the recovery image at:
```
out/target/product/RMX3771/recovery.img
```

## Installation

### Prerequisites
1. Unlocked bootloader
2. USB debugging enabled
3. ADB and Fastboot installed on your PC

### Flash TWRP

#### Method 1: Using Fastboot

```bash
# Reboot to fastboot mode
adb reboot bootloader

# Flash TWRP
fastboot flash recovery recovery.img

# Reboot to recovery
fastboot reboot recovery
```

#### Method 2: Temporary Boot (No Install)

```bash
# Reboot to fastboot mode
adb reboot bootloader

# Boot TWRP temporarily (won't replace stock recovery)
fastboot boot recovery.img
```

#### Method 3: Flash via existing TWRP/Custom Recovery

If you already have TWRP or another custom recovery:
1. Copy `recovery.img` to your device
2. Boot into TWRP
3. Go to Install → Install Image
4. Select the recovery.img file
5. Select "Recovery" partition
6. Swipe to flash

### Important Notes

⚠️ **WARNING**: 
- Unlocking bootloader will **WIPE ALL DATA**
- Make sure to backup your important data before proceeding
- This is for advanced users only

## Decryption

This TWRP build supports FBE (File-Based Encryption) decryption. When you boot into TWRP:
1. You'll see a password prompt
2. Enter your lock screen password/PIN/pattern
3. TWRP will decrypt /data partition

If decryption fails:
- Make sure you're using the correct password
- Try rebooting to system and back to recovery
- Format data (this will erase everything)

## Troubleshooting

### Build Issues

**Error: "make: command not found"**
```bash
sudo apt-get install build-essential
```

**Error: "repo: command not found"**
```bash
export PATH=~/bin:$PATH
```

**Error: Out of memory during build**
- Reduce the number of parallel jobs: `mka recoveryimage -j4`
- Close other applications
- Add swap space

### TWRP Issues

**Touch not working**
- The device tree includes touch drivers, but if it doesn't work, you may need to add additional drivers

**Display issues**
- Check brightness path in BoardConfig.mk
- Verify display resolution settings

**Decryption not working**
- Make sure you have the correct password
- Check if your ROM uses custom encryption
- Try formatting data (WARNING: This erases everything)

**MTP not working**
- Make sure to enable MTP in TWRP settings
- Try different USB ports/cables

## Partition Layout

| Partition | Size | Type | Description |
|-----------|------|------|-------------|
| boot | 64 MB | emmc | Kernel and ramdisk |
| recovery | 64 MB | emmc | Recovery partition |
| dtbo | Variable | emmc | Device Tree Blob Overlay |
| vbmeta | Small | emmc | Verified Boot Metadata |
| super | ~9 GB | emmc | Super partition (contains system, vendor, product, system_ext, odm) |
| userdata | Variable | f2fs/ext4 | User data and apps |
| metadata | Small | ext4 | Encryption metadata |

## Credits

- **TeamWin Recovery Project** - For TWRP
- **LineageOS Team** - For device tree references
- **Realme Community** - For device support
- **MediaTek Community** - For MTK-specific fixes

## Maintainer

- Your Name (@YourGitHub)

## Donate

If you find this useful, consider supporting the developers:
- [TeamWin Recovery Project](https://twrp.me/donate/)

## License

```
Copyright (C) 2024 TeamWin Recovery Project

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
