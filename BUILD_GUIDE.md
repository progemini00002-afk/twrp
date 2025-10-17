# Quick Build Guide - TWRP for Realme 11 Pro 5G (RMX3771)

## What You Have Right Now

✅ **Device Tree Created**: `device/realme/RMX3771/`
✅ **Kernel Extracted**: From your boot.img
✅ **Configuration Files**: BoardConfig.mk, device.mk, etc.
✅ **Recovery Partition Layout**: Configured for your device

## Building TWRP - Step by Step

### Option 1: Build on Linux (Recommended)

#### Step 1: Set Up Linux Environment

You need Ubuntu 20.04 or newer. You can use:
- Native Linux installation
- Dual boot
- Virtual Machine (VMware/VirtualBox) - Needs at least 200GB disk space
- WSL2 on Windows (slower but works)

#### Step 2: Install Required Packages

```bash
sudo apt-get update && sudo apt-get install -y \
    bc bison build-essential ccache curl flex g++-multilib gcc-multilib \
    git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev \
    lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev \
    libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools \
    xsltproc zip zlib1g-dev python-is-python3 openjdk-11-jdk \
    android-tools-adb android-tools-fastboot
```

#### Step 3: Install repo

```bash
mkdir -p ~/bin
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
echo 'export PATH=~/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

#### Step 4: Initialize TWRP Source

```bash
# Create working directory
mkdir -p ~/twrp
cd ~/twrp

# Configure git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Initialize TWRP 12.1 manifest
repo init -u https://github.com/minimal-manifest-twrp/platform_manifest_twrp_aosp.git -b twrp-12.1

# Sync repositories (This will download ~30-40 GB, takes 1-3 hours)
repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags
```

#### Step 5: Copy Device Tree

Transfer the `device` folder from Windows to your Linux environment:

**If using WSL2:**
```bash
# In WSL2, your Windows drives are mounted at /mnt/
cp -r /mnt/c/Users/RDP/Desktop/sunny/device ~/twrp/
```

**If using Virtual Machine or separate Linux:**
- Use shared folders, USB drive, or file transfer
- Copy the `device/realme/RMX3771` folder to `~/twrp/device/realme/RMX3771`

**Or create it directly in Linux:**
```bash
# You can also clone from GitHub after uploading
cd ~/twrp
git clone YOUR_GITHUB_REPO device/realme/RMX3771
```

#### Step 6: Build TWRP

```bash
cd ~/twrp

# Set up environment
source build/envsetup.sh

# Select your device (choose twrp_RMX3771-eng from the list)
lunch twrp_RMX3771-eng

# Start building (takes 30 minutes to 2 hours depending on your PC)
mka recoveryimage -j$(nproc --all)
```

#### Step 7: Get Your Recovery Image

If build is successful, your recovery image will be at:
```
~/twrp/out/target/product/RMX3771/recovery.img
```

Copy it back to Windows:
```bash
# If using WSL2
cp out/target/product/RMX3771/recovery.img /mnt/c/Users/RDP/Desktop/
```

---

### Option 2: Use GitHub Actions (Cloud Build)

If you don't have a Linux machine or don't want to download 40GB:

1. **Upload device tree to GitHub**
2. **Use TWRP Build Action workflow**
3. **Download built recovery.img from GitHub releases**

I can create the GitHub Actions workflow file if you want this option.

---

## Flashing TWRP to Your Device

### Prerequisites

⚠️ **WARNING**: Unlocking bootloader will ERASE ALL DATA!

1. **Backup everything important**
2. **Enable USB Debugging**:
   - Settings → About Phone → Tap "Build Number" 7 times
   - Settings → Developer Options → Enable "USB Debugging"
   - Settings → Developer Options → Enable "OEM Unlocking"

3. **Unlock Bootloader**:
   ```bash
   # Boot to fastboot
   adb reboot bootloader
   
   # Unlock bootloader (THIS WIPES DATA!)
   fastboot flashing unlock
   
   # Or for some Realme devices:
   fastboot oem unlock
   ```

### Flash TWRP

```bash
# Make sure your device is in fastboot mode
adb reboot bootloader

# Flash TWRP
fastboot flash recovery recovery.img

# Reboot to recovery
fastboot reboot recovery
```

### First Boot

1. Device will reboot to TWRP
2. You'll see a password prompt - enter your lock screen password
3. TWRP will decrypt your data partition
4. You're in TWRP! 🎉

---

## What Can You Do in TWRP?

✅ **Install Custom ROMs** - Flash ZIP files
✅ **Backup/Restore** - Complete device backup
✅ **Wipe Data** - Factory reset
✅ **Root Device** - Flash Magisk
✅ **Install Mods** - GApps, kernels, etc.
✅ **File Manager** - Browse device files
✅ **Terminal** - Run commands
✅ **ADB Access** - Use ADB commands from PC

---

## Troubleshooting

### Build Errors

**"No rule to make target 'recoveryimage'"**
- Make sure you ran `lunch twrp_RMX3771-eng`
- Check that device tree is in correct location

**"kernel: not found"**
- Make sure `device/realme/RMX3771/prebuilt/kernel` exists
- Re-run `extract_kernel.py` if needed

**Out of memory**
- Reduce parallel jobs: `mka recoveryimage -j4`
- Add swap space

### Flashing Errors

**"FAILED (remote: Partition not found)"**
- Your device might use different partition names
- Try: `fastboot flash recovery_a recovery.img` and `fastboot flash recovery_b recovery.img`

**"FAILED (remote: Command not allowed)"**
- Bootloader is locked - unlock it first

**Device boots to system instead of TWRP**
- Some ROMs replace TWRP on boot
- Try: `fastboot boot recovery.img` (temporary boot)
- Or disable dm-verity/force-encrypt

---

## Next Steps

1. ✅ **Build TWRP** using this guide
2. ✅ **Test TWRP** on your device
3. ✅ **Report Issues** if something doesn't work
4. ✅ **Share** with Realme 11 Pro community
5. ✅ **Upload to GitHub** for others to use

---

## Need Help?

- **XDA Forums**: Post in Realme 11 Pro section
- **Telegram**: Join Realme modding groups
- **GitHub Issues**: Report device tree issues

---

## Files in This Package

```
device/realme/RMX3771/
├── AndroidProducts.mk          # Product definitions
├── BoardConfig.mk              # Board configuration (most important)
├── device.mk                   # Device-specific makefiles
├── twrp_RMX3771.mk            # TWRP product config
├── vendorsetup.sh             # Lunch combo setup
├── README.md                   # Device tree documentation
├── recovery/
│   └── root/
│       └── system/
│           └── etc/
│               ├── recovery.fstab    # Partition mounting
│               └── twrp.flags        # TWRP partition flags
└── prebuilt/
    ├── kernel                  # Extracted kernel
    └── ramdisk.img            # Extracted ramdisk
```

---

## Building Tips

🚀 **Speed Up Builds**:
```bash
# Use ccache
export USE_CCACHE=1
export CCACHE_DIR=~/.ccache
ccache -M 50G
```

💾 **Save Bandwidth**:
- Use `--depth=1` for shallow clones
- Sync only what you need

⚡ **Parallel Build**:
- More cores = faster build
- But don't use all cores if low on RAM
- Safe: `mka recoveryimage -j$(($(nproc)-2))`

---

**Good luck building TWRP! 🎉**
