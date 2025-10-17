# 🔧 TWRP Device Tree for Realme 11 Pro 5G (RMX3771)

[![Build TWRP](https://github.com/YOUR_USERNAME/android_device_realme_RMX3771/workflows/Build%20TWRP%20Recovery/badge.svg)](https://github.com/YOUR_USERNAME/android_device_realme_RMX3771/actions)
[![TWRP Version](https://img.shields.io/badge/TWRP-12.1-blue.svg)](https://twrp.me/)
[![Android](https://img.shields.io/badge/Android-13-green.svg)](https://www.android.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Complete TWRP device tree for building Team Win Recovery Project for the **Realme 11 Pro 5G** (RMX3771).

![Realme 11 Pro 5G](https://fdn2.gsmarena.com/vv/bigpic/realme-11-pro-5g.jpg)

## 📱 Device Specifications

| Feature | Specification |
|---------|---------------|
| **Device** | Realme 11 Pro 5G |
| **Codename** | RMX3771 |
| **Manufacturer** | Realme |
| **Chipset** | MediaTek Dimensity 7050 (6nm) |
| **CPU** | Octa-core (2x2.6 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55) |
| **GPU** | Mali-G68 MC4 |
| **Memory** | 8GB / 12GB RAM |
| **Storage** | 128GB / 256GB UFS 3.1 |
| **Battery** | 5000 mAh, 67W SUPERVOOC |
| **Display** | 6.7" AMOLED, 1080x2412, 120Hz |
| **Camera** | 100MP (main) + 2MP (depth) |
| **Android** | Android 13, Realme UI 5.0 |
| **Architecture** | ARM64 |

## ✨ Features

- ✅ **Decryption Support** - FBE (File-Based Encryption) with metadata
- ✅ **MTP Support** - Transfer files to/from PC
- ✅ **USB OTG** - Use external USB drives
- ✅ **Backup/Restore** - Complete NANDROID backups
- ✅ **Flash ZIPs** - Install ROMs, Magisk, mods
- ✅ **ADB Access** - Terminal and shell commands
- ✅ **Brightness Control** - Adjust screen brightness
- ✅ **Vibration** - Haptic feedback support
- ✅ **Dynamic Partitions** - Full support for super partition
- ✅ **Logcat** - Advanced debugging

---

## 🚀 Quick Start

### Option 1: Download Pre-built Recovery

1. Go to [Releases](https://github.com/YOUR_USERNAME/android_device_realme_RMX3771/releases)
2. Download `recovery.img`
3. Flash using fastboot (see installation below)

### Option 2: Build from Source

Detailed instructions in **[BUILD_GUIDE.md](BUILD_GUIDE.md)**

```bash
# Quick build commands
mkdir ~/twrp && cd ~/twrp
repo init -u https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp.git -b twrp-12.1
repo sync -j$(nproc --all)
git clone https://github.com/YOUR_USERNAME/android_device_realme_RMX3771 device/realme/RMX3771
source build/envsetup.sh
lunch twrp_RMX3771-eng
mka recoveryimage
```

---

## 📦 Installation

### Prerequisites

⚠️ **WARNING**: Unlocking bootloader will **ERASE ALL DATA**!

1. **Backup your data**
2. **Enable USB Debugging**:
   - Settings → About Phone → Tap "Build Number" 7 times
   - Settings → Developer Options → Enable USB Debugging
   - Settings → Developer Options → Enable OEM Unlocking

### Unlock Bootloader

```bash
adb reboot bootloader
fastboot flashing unlock
# Or: fastboot oem unlock
```

### Flash TWRP

```bash
# Flash to recovery partition
fastboot flash recovery recovery.img

# Reboot to recovery
fastboot reboot recovery
```

### Alternative: Boot Without Installing

```bash
# Temporary boot (doesn't replace stock recovery)
fastboot boot recovery.img
```

---

## 📁 Repository Structure

```
device/realme/RMX3771/
├── AndroidProducts.mk       # Product definitions
├── BoardConfig.mk           # Board & kernel config
├── device.mk                # Device makefiles
├── twrp_RMX3771.mk         # TWRP product config
├── vendorsetup.sh          # Lunch combo setup
├── README.md                # Device documentation
├── recovery/
│   └── root/system/etc/
│       ├── recovery.fstab   # Partition table
│       └── twrp.flags       # TWRP flags
└── prebuilt/
    ├── kernel               # Prebuilt kernel
    └── ramdisk.img         # Ramdisk
```

---

## 🔧 Configuration Details

### Boot Image Information
- **Header Version**: 4 (Android 13+)
- **Kernel Base**: 0x40078000
- **Page Size**: 2048 bytes
- **DTB**: Included in boot image

### Partitions
- **Super Partition**: ~9 GB (dynamic)
  - system, vendor, product, system_ext, odm
- **Boot/Recovery**: 64 MB each
- **Userdata**: F2FS with FBE encryption
- **Metadata**: For encryption keys

---

## 🐛 Troubleshooting

### Build Issues

**Problem**: "kernel: not found"  
**Solution**: Make sure prebuilt kernel exists in `device/realme/RMX3771/prebuilt/kernel`

**Problem**: "No rule to make target 'recoveryimage'"  
**Solution**: Run `lunch twrp_RMX3771-eng` before building

**Problem**: Out of memory  
**Solution**: Reduce parallel jobs: `mka recoveryimage -j4`

### Device Issues

**Problem**: Can't unlock bootloader  
**Solution**: Wait 7 days after enabling OEM unlock, or use Realme's unlock tool

**Problem**: TWRP doesn't boot  
**Solution**: Try `fastboot boot recovery.img` instead of flashing

**Problem**: Decryption fails  
**Solution**: Enter correct password, or format data (wipes everything)

---

## 📚 Documentation

- **[BUILD_GUIDE.md](BUILD_GUIDE.md)** - Complete build instructions
- **[SETUP_SUMMARY.md](SETUP_SUMMARY.md)** - Project overview
- **[device/realme/RMX3771/README.md](device/realme/RMX3771/README.md)** - Device tree docs

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

---

## 👥 Credits

- **[TeamWin Recovery Project](https://twrp.me/)** - For TWRP
- **MediaTek Community** - For MTK device support  
- **Realme Community** - For device information
- **XDA Developers** - For guides and support

---

## 📢 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/android_device_realme_RMX3771/issues)
- **XDA Thread**: [Link to XDA thread]
- **Telegram**: [Link to Telegram group]

---

## 📝 License

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

---

## ⭐ Star History

If this project helped you, please give it a ⭐!

---

**Made with ❤️ for Realme 11 Pro 5G users**
