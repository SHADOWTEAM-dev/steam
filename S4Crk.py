import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Start with a stylish branding message with color
print(Fore.GREEN + "=" * 39)
print(Fore.CYAN + "        S4Crk - By SHADOWTEAM         ")
print(Fore.GREEN + "     A Revolutionary Tool for DLL    ")
print(Fore.GREEN + "     Manipulation - Be Responsible!  ")
print(Fore.GREEN + "=" * 39)
print(Fore.RED + "WARNING: This tool is provided 'as-is' for educational purposes only.")
print(Fore.RED + "By using this software, you assume full responsibility for any consequences,")
print(Fore.RED + "including data loss, corruption, or violations of terms of service.")
print(Fore.RED + "The creator (SHADOWTEAM) is NOT liable for any damages or issues.")
print(Fore.GREEN + "=" * 39)

def get_file_path(file_name, required=True):
    # Open the file selection window
    root = tk.Tk()
    root.withdraw()  # Hide the window
    file_path = filedialog.askopenfilename(title=f"Select {file_name}", filetypes=[("DLL Files", "*.dll")])
    
    while required and not file_path:
        messagebox.showerror("Error", f"{file_name} is required!")
        file_path = filedialog.askopenfilename(title=f"Select {file_name}", filetypes=[("DLL Files", "*.dll")])
    
    return file_path

def replace_dll(original_path, new_path):
    if not original_path or not os.path.exists(original_path):
        print(Fore.RED + "No original file found, skipping...")
        return
    
    if not os.path.exists(new_path):
        print(Fore.RED + f"New DLL not found: {new_path}, skipping...")
        return
    
    backup_path = original_path + ".bak"
    if not os.path.exists(backup_path):
        shutil.copy2(original_path, backup_path)
    
    try:
        shutil.copy2(new_path, original_path)
        print(Fore.GREEN + f"✔️ Successfully replaced: {os.path.basename(original_path)}")
    except Exception as e:
        print(Fore.RED + f"❌ Error replacing {os.path.basename(original_path)}: {e}")
        print(Fore.YELLOW + "Restoring backup...")
        shutil.copy2(backup_path, original_path)
        print(Fore.YELLOW + "Backup restored.")

def main():
    print(Fore.GREEN + "=" * 39)
    print(Fore.CYAN + "Preparing to Replace DLLs...")

    # Select steamapi64.dll
    steamapi64_path = get_file_path("STEAMAPI64.DLL", required=True)

    # Ask the user if they want to select steamapi.dll
    root = tk.Tk()
    root.withdraw()  # Hide the window
    response = messagebox.askyesno("Confirm", "Do you want to select STEAMAPI.DLL?")
    
    if response:
        steamapi_path = get_file_path("STEAMAPI.DLL", required=False)
    else:
        steamapi_path = None
        print(Fore.YELLOW + "STEAMAPI.DLL not selected, skipping...")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    dll_folder = os.path.join(script_dir, "dlls")
    new_steamapi64_path = os.path.join(dll_folder, "steam_api64.dll")
    new_steamapi_path = os.path.join(dll_folder, "steam_api.dll")
    
    replace_dll(steamapi64_path, new_steamapi64_path)
    
    if steamapi_path:
        replace_dll(steamapi_path, new_steamapi_path)
    
    # After completion, inform the user
    messagebox.showinfo("Process Complete", "DLL replacement complete. The program will now exit.")
    
    # Close the Tkinter window
    root.quit()

if __name__ == "__main__":
    main()
