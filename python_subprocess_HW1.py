import subprocess
import re
import argparse

def run_script(num, xx):
    cmd = ['python', 'your_script.py', '--num', str(num), '--xx', str(xx)]
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

    total_sum = 0

    # First run
    output_first_run = run_script(100, 90)
    sum_first_run = extract_and_sum(output_first_run)
    total_sum += sum_first_run
    print(f"Sum of values in the first run: {sum_first_run}")

    # Second run
    output_second_run = run_script(-10, -90)
    sum_second_run = extract_and_sum(output_second_run)
    total_sum += sum_second_run
    print(f"Sum of values in the second run: {sum_second_run}")

    # Third run
    output_third_run = run_script(10, 0)  # Adjust values as needed
    sum_third_run = extract_and_sum(output_third_run)
    total_sum += sum_third_run
    print(f"Sum of values in the third run: {sum_third_run}")

    print(f"Total sum across all runs: {total_sum}")

if __name__ == "__main__":
    main()
