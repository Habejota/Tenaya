from time import sleep as delay
from os import system as shell
from os import chdir, getcwd
import sys

disk_partition = "0x800-1x300"

shell("cls")
print("0x800-1x300: VGA Bios is starting...")
print("")
print("[  OK  ] Building kernel in diretory: /os --install")
print("[  OK  ] Compiling dependences Kernel modules. . ."),  delay(1.000)
print('         Building OS Bridge: /network/ifstat/route/drivers/efi.exe --cache "/os/tmp/boot.tmp"')
print("         Setting implemented Interfaces...", end=""), delay(1)
print("done.") 
print("[  OK  ] Window layout begin drawing (safe graphics)...")
print("[DEPEND] Mounting External devices Drivers. . ."), delay(1.111)

try: 
    kernel = open(r"os\kernel.py", "rt")
except FileNotFoundError:
    print("[ FAIL ] Not readed an runner os installed at PS/2 port!")
    print("         Kernel device is not started!")
    shell("python network.py")
else:
    print("[  OK  ] Running tasks: 0x800-1x300/os/kernel.py --login -i")
    print("         Charging config.ini - [0x800-1x300/os/kernel.py --loadLibraries]")
    print("         Command Prompt startup Device!")
    chdir("os")
    shell(r"python kernel.py")