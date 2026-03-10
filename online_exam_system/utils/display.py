"""
utils/display.py — Terminal display helpers
"""
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    print("=" * 56)
    print("    ONLINE EXAMINATION & EVALUATION SYSTEM")
    print("    Version 1.0  |  Academic Edition")
    print("=" * 56)


def print_header(title: str):
    print("\n" + "=" * 50)
    print(f"   {title.upper()}")
    print("=" * 50)


def print_success(msg: str):
    print(f"\n  [✓] {msg}")


def print_error(msg: str):
    print(f"\n  [✗] {msg}")


def print_info(msg: str):
    print(f"\n  [i] {msg}")


def divider():
    print("  " + "-" * 46)
