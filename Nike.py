import os
import time

OUTDIR = "/sdcard/Download/ffhack_cpp/"
os.makedirs(OUTDIR, exist_ok=True)

# ==== CODE CHỨC NĂNG DẠNG C++ (tách riêng như file .cpp/.h) ====

code_regedit_cpp = """
// regedit.cpp - Fake recoil giảm giật + headlock nhẹ
void applyRegedit() {
    float recoil = 0.3f;
    bool headLock = true;
    float sensitivity = 2.5f;
    // apply to weapon logic...
}
"""

code_aimlock_cpp = """
// aimlock.cpp - Tự khóa đầu nhẹ khi nhắm địch
struct AimConfig {
    bool lockHead = true;
    float smooth = 0.4f;
    float delay = 0.1f;
    const char* range = "close";
};
"""

code_feedback_cfg = """
// feedback.cfg - Hệ thống khóa đầu khi tâm trùng đầu địch
[feedback_system]
enable_lock_on=true
target=smart
auto_lock_when_on_head=true
"""

code_dpi_reg = """
// dpi2440.reg - Cấu hình cảm ứng cao 2440Hz
[touch_config]
touch_rate=2440
sensitivity=2.0
priority=high
"""

code_antiban_h = """
// antiban.h - Fake ID chống sảnh, chống ban
#define DEVICE_ID "ID_SAFE_9999"
#define PLAYER_ID "ID_SAFE_9999"
"""

# ==== HÀM GHI FILE ====
def write_file(filename, content):
    path = os.path.join(OUTDIR, filename)
    try:
        with open(path, "w") as f:
            f.write(content)
        print(f"[✓] Ghi thành công: {filename}")
    except Exception as e:
        print(f"[✘] Lỗi ghi {filename}: {e}")

# ==== CÀI TỪNG CHỨC NĂNG ====
def install_regedit():
    write_file("regedit.cpp", code_regedit_cpp)

def install_aimlock():
    write_file("aimlock.cpp", code_aimlock_cpp)

def install_feedback():
    write_file("feedback.cfg", code_feedback_cfg)

def install_dpi():
    write_file("dpi2440.reg", code_dpi_reg)

def install_antiban():
    write_file("antiban.h", code_antiban_h)

def install_full():
    install_regedit()
    install_aimlock()
    install_feedback()
    install_dpi()
    install_antiban()

# ==== MENU ====
def banner():
    os.system("clear")
    print("🔥 TOOL XUẤT FILE HACK FF C++ | OB49 🔥")
    print(f"📁 Lưu tại: {OUTDIR}\n")

def main():
    while True:
        banner()
        print("1. Xuất file C++ Regedit")
        print("2. Xuất file Aimlock.cpp")
        print("3. Xuất feedback.cfg")
        print("4. Xuất dpi2440.reg")
        print("5. Xuất antiban.h")
        print("6. Xuất toàn bộ (Full hack)")
        print("0. Thoát\n")
        ch = input("Chọn chức năng: ").strip()
        if ch == "1":
            install_regedit()
        elif ch == "2":
            install_aimlock()
        elif ch == "3":
            install_feedback()
        elif ch == "4":
            install_dpi()
        elif ch == "5":
            install_antiban()
        elif ch == "6":
            install_full()
        elif ch == "0":
            print("Tạm biệt!")
            break
        else:
            print("[!] Chọn sai!")
        time.sleep(1)

if __name__ == "__main__":
    main()
