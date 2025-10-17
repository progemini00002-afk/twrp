#!/usr/bin/env python3
"""
Extract kernel and DTB from boot.img for TWRP building
"""

import os
import struct
import sys

def extract_boot_components(boot_img_path, output_dir="device/realme/RMX3771/prebuilt"):
    """Extract kernel, ramdisk, and dtb from boot image"""
    
    if not os.path.exists(boot_img_path):
        print(f"Error: {boot_img_path} not found!")
        return False
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        with open(boot_img_path, 'rb') as f:
            # Read header
            header = f.read(1660)
            
            # Check magic
            magic = header[0:8]
            if magic != b'ANDROID!':
                print("Not a valid Android boot image!")
                return False
            
            # Parse header
            kernel_size = struct.unpack('<I', header[8:12])[0]
            kernel_addr = struct.unpack('<I', header[12:16])[0]
            ramdisk_size = struct.unpack('<I', header[16:20])[0]
            ramdisk_addr = struct.unpack('<I', header[20:24])[0]
            second_size = struct.unpack('<I', header[24:28])[0]
            second_addr = struct.unpack('<I', header[28:32])[0]
            tags_addr = struct.unpack('<I', header[32:36])[0]
            page_size = struct.unpack('<I', header[36:40])[0]
            header_version = struct.unpack('<I', header[40:44])[0]
            
            print(f"Boot image header version: {header_version}")
            print(f"Kernel size: {kernel_size} bytes")
            print(f"Ramdisk size: {ramdisk_size} bytes")
            print(f"Second stage size: {second_size} bytes")
            print(f"Page size: {page_size} bytes")
            
            # For header v4, page_size might be 0, use default 4096
            if page_size == 0:
                page_size = 4096
                print(f"Using default page size: {page_size}")
            
            # Calculate offsets
            kernel_offset = page_size
            ramdisk_offset = kernel_offset + ((kernel_size + page_size - 1) // page_size) * page_size
            second_offset = ramdisk_offset + ((ramdisk_size + page_size - 1) // page_size) * page_size
            
            # Extract kernel
            f.seek(kernel_offset)
            kernel_data = f.read(kernel_size)
            kernel_path = os.path.join(output_dir, "kernel")
            with open(kernel_path, 'wb') as kf:
                kf.write(kernel_data)
            print(f"✓ Kernel extracted to: {kernel_path}")
            
            # Extract ramdisk (if exists)
            if ramdisk_size > 0:
                f.seek(ramdisk_offset)
                ramdisk_data = f.read(ramdisk_size)
                ramdisk_path = os.path.join(output_dir, "ramdisk.img")
                with open(ramdisk_path, 'wb') as rf:
                    rf.write(ramdisk_data)
                print(f"✓ Ramdisk extracted to: {ramdisk_path}")
            
            # Extract second stage (DTB if exists)
            if second_size > 0:
                f.seek(second_offset)
                second_data = f.read(second_size)
                dtb_path = os.path.join(output_dir, "dtb.img")
                with open(dtb_path, 'wb') as df:
                    df.write(second_data)
                print(f"✓ DTB extracted to: {dtb_path}")
            
            # For header v1+, check for recovery dtbo
            if header_version >= 1:
                recovery_dtbo_size = struct.unpack('<I', header[1584:1588])[0]
                if recovery_dtbo_size > 0:
                    recovery_dtbo_offset = struct.unpack('<Q', header[1588:1596])[0]
                    f.seek(recovery_dtbo_offset)
                    dtbo_data = f.read(recovery_dtbo_size)
                    dtbo_path = os.path.join(output_dir, "dtbo.img")
                    with open(dtbo_path, 'wb') as df:
                        df.write(dtbo_data)
                    print(f"✓ DTBO extracted to: {dtbo_path}")
            
            # For header v2+, check for DTB
            if header_version >= 2:
                dtb_size = struct.unpack('<I', header[1600:1604])[0]
                if dtb_size > 0:
                    # DTB is appended after everything else
                    dtb_offset = second_offset + ((second_size + page_size - 1) // page_size) * page_size
                    f.seek(dtb_offset)
                    dtb_data = f.read(dtb_size)
                    dtb_path = os.path.join(output_dir, "dtb.img")
                    with open(dtb_path, 'wb') as df:
                        df.write(dtb_data)
                    print(f"✓ DTB (v2) extracted to: {dtb_path}")
            
            print("\n✓ All components extracted successfully!")
            print(f"\nNext steps:")
            print(f"1. Review the extracted files in: {output_dir}")
            print(f"2. The device tree is ready at: device/realme/RMX3771")
            print(f"3. To build TWRP, you need to set up the TWRP build environment")
            
            return True
            
    except Exception as e:
        print(f"Error extracting boot components: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    boot_img = "boot.img"
    
    if not os.path.exists(boot_img):
        print(f"Error: {boot_img} not found!")
        print(f"Please make sure boot.img is in the current directory")
        sys.exit(1)
    
    success = extract_boot_components(boot_img)
    sys.exit(0 if success else 1)
