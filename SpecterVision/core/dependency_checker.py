import sys
import subprocess
import importlib.util
from config.banner import print_success, print_error, print_info, print_warning, Colors

DEPENDENCIES = {
    'flask': 'Flask==3.0.0',
    'flask_cors': 'flask-cors==4.0.0',
    'cv2': 'opencv-python==4.8.1.78',
    'PIL': 'Pillow==10.1.0',
    'requests': 'requests==2.31.0',
    'pyngrok': 'pyngrok==7.0.5'
}

def is_package_installed(package_name):
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def install_package(pip_package):
    print_info(f"Installing {pip_package}...")
    try:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', pip_package, '--quiet'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies(silent=False):
    if not silent:
        print_info("Checking system dependencies...")
        print()

    all_installed = True
    installed_count = 0
    missing_count = 0

    for module_name, pip_package in DEPENDENCIES.items():
        package_display = pip_package.split('==')[0]

        if is_package_installed(module_name):
            if not silent:
                print(f"  {Colors.GREEN}✓{Colors.RESET} {package_display:<20} {Colors.GREEN}[INSTALLED]{Colors.RESET}")
            installed_count += 1
        else:
            if not silent:
                print(f"  {Colors.YELLOW}⚠{Colors.RESET} {package_display:<20} {Colors.YELLOW}[MISSING]{Colors.RESET}")
            missing_count += 1
            all_installed = False

            if silent:
                if install_package(pip_package):
                    installed_count += 1
                    missing_count -= 1
            else:
                print_info(f"Installing {package_display}...")
                if install_package(pip_package):
                    print_success(f"{package_display} installed successfully")
                else:
                    print_error(f"Failed to install {package_display}")

    if not silent:
        print()
        print(f"  Total: {Colors.CYAN}{installed_count} installed{Colors.RESET}, {Colors.YELLOW}{missing_count} missing{Colors.RESET}")
        print()

    return all_installed or missing_count == 0

def check_dependencies_status():
    print()
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print(f"{Colors.BOLD}  SYSTEM DEPENDENCIES STATUS{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*64}{Colors.RESET}")
    print()

    check_and_install_dependencies(silent=False)

    print_info("Press Enter to return to main menu...")
    input()
