import sys
from .diff_analyzer import get_git_diff
from .message_generator import generate_message

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Usage: git-scribe [options]")
        return

    diff = get_git_diff()
    message = generate_message(diff)
    print(f"Proposed commit message: {message}")

if __name__ == '__main__':
    main()