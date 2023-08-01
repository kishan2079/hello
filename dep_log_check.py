def filter_error_logs(input_file, output_file):
    error_logs = []

    with open(input_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                error_logs.append(line)

    with open(output_file, 'w') as file:
        for log in error_logs:
            file.write(log)

filter_error_logs('console.log','error_logs.txt')