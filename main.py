import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Run different LLM models")
    parser.add_argument('--model', choices=['deepseek', 'chatgpt'], required=True, help="Choose which model to run")
    parser.add_argument("--test",  action='store_true', help="Run the debug prompt for testing")
    parser.add_argument('--version', type=int, choices=[4, 3], default = 4, required=False, help="ChatGPT model version")

    args = parser.parse_args()
    root_dir = os.path.dirname(os.path.abspath(__file__))

    if args.model == 'deepseek':
        sys.path.insert(0, os.path.join(root_dir, 'deepseek'))
        from util.deepseek import run_deepseek
        run_deepseek(args.test)

    elif args.model == 'chatgpt':
        sys.path.insert(0, os.path.join(root_dir, 'chatgpt'))
        from util.chatgpt import run_chatgpt
        run_chatgpt(args.test, args.version)

if __name__ == "__main__":
    main()