# 🚀 TWRP Quick Reference - Realme 11 Pro 5G (RMX3771)

## 📋 Essential Information

**Device**: Realme 11 Pro 5G  
**Codename**: RMX3771  
**TWRP Version**: 12.1  
**Android**: 13  
**Chipset**: MediaTek Dimensity 7050

---

## ⚡ Quick Commands

### Build TWRP (Linux)
```bash
cd ~/twrp
source build/envsetup.sh
lunch twrp_RMX3771-eng
mka recoveryimage
```

### Flash TWRP
```bash
adb reboot bootloader
fastboot flash recovery recovery.img
fastboot reboot recovery
```

### Unlock Bootloader
```bash
adb reboot bootloader
fastboot flashing unlock
```

---

## 📁 File Locations

| Item | Path |
|------|------|
| Device Tree | `device/realme/RMX3771/` |
| Kernel | `device/realme/RMX3771/prebuilt/kernel` |
| Recovery Output | `out/target/product/RMX3771/recovery.img` |
| Build Guide | `BUILD_GUIDE.md` |
| Setup Summary | `SETUP_SUMMARY.md` |

---

## 🔧 Important Files

| File | Purpose |
|------|---------|
| `BoardConfig.mk` | Board & kernel config |
| `device.mk` | Device settings |
| `recovery.fstab` | Partition layout |
| `twrp.flags` | TWRP partition flags |

---

## 📚 Documentation

| Document | When to Use |
|----------|-------------|
| `README.md` | Project overview |
| `BUILD_GUIDE.md` | Step-by-step build instructions |
| `SETUP_SUMMARY.md` | Complete project summary |
| `COMPLETION_REPORT.md` | Technical details & status |

---

## ⚙️ Key Configurations

```makefile
# Device
TARGET_ARCH := arm64
TARGET_BOARD_PLATFORM := mt6877

# Boot
BOARD_BOOTIMG_HEADER_VERSION := 4
BOARD_KERNEL_BASE := 0x40078000
BOARD_KERNEL_PAGESIZE := 2048

# Partitions
BOARD_SUPER_PARTITION_SIZE := 9126805504
BOARD_USES_METADATA_PARTITION := true

# Encryption
TW_INCLUDE_CRYPTO := true
TW_INCLUDE_CRYPTO_FBE := true
```

---

## 🐛 Common Issues

| Problem | Solution |
|---------|----------|
| Kernel not found | Check `device/realme/RMX3771/prebuilt/kernel` |
| Can't build | Run `lunch twrp_RMX3771-eng` |
| Out of memory | Use `mka recoveryimage -j4` |
| Bootloader locked | Run `fastboot flashing unlock` |
| TWRP won't boot | Try `fastboot boot recovery.img` |

---

## 🔗 Quick Links

- **TWRP Official**: https://twrp.me/
- **Manifest**: https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp
- **XDA Forums**: Search "Realme 11 Pro RMX3771"

---

## 📞 Need Help?

1. Check `BUILD_GUIDE.md` for detailed instructions
2. Check `SETUP_SUMMARY.md` for troubleshooting
3. Create GitHub issue
4. Ask on XDA Forums or Telegram

---

**Created**: October 17, 2025  
**Status**: ✅ Ready to Build
