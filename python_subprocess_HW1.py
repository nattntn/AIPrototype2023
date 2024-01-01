import subprocess
import re
import argparse

def run_script(num, xx):
    cmd = ['python', 'firstpy.py', '--num', str(num), '--xx', str(xx)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    return output

def extract_and_sum(output):
    matches = re.findall(r'we are in the main function\n(\S+)', output)
    values = [int(match) for match in matches]
    return sum(values)

def main():
    parser = argparse.ArgumentParser(description='Run the script with inputs --num and --xx.')
    parser.add_argument('--num', type=int, help='Input value num')
    parser.add_argument('--xx', type=int, help='Input value xx')
    args = parser.parse_args()

    output = run_script(args.num, args.xx)
    sum_values = extract_and_sum(output)

    print(f"Sum of values in the run with num={args.num} and xx={args.xx}: {sum_values}")

if __name__ == "__main__":
    python run_script.py --num 100 --xx 90
    python run_script.py --num -10 --xx -90
    python run_script.py --num 0

