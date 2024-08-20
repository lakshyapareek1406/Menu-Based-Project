# Access log from the cloud


#!/usr/bin/env python3
import cgi
import boto3
import json

# Hardcoded AWS credentials (not recommended for production, use environment variables or IAM roles)
aws_access_key_id = 'Ayour key'
aws_secret_access_key = 'your secret key'

# Function to fetch CloudWatch logs
def fetch_logs(log_group_name, log_stream_name, region_name):
    try:
        client = boto3.client('logs',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              region_name=region_name)

        response = client.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            limit=10  # Adjust as needed
        )

        logs = []
        for event in response['events']:
            logs.append({
                'timestamp': event['timestamp'],
                'message': event['message']
            })

        return logs

    except Exception as e:
        return {'error': str(e)}

# Main CGI script handling
def main():
    print("Content-Type: application/json")
    print()  # Blank line required, end of headers

    form = cgi.FieldStorage()
    log_group_name = form.getvalue('log_group_name')
    log_stream_name = form.getvalue('log_stream_name')
    region_name = form.getvalue('region_name')

    if not log_group_name or not log_stream_name or not region_name:
        print(json.dumps({'error': 'Missing parameters'}))
        return

    logs = fetch_logs(log_group_name, log_stream_name, region_name)
    print(json.dumps(logs))

if __name__ == '__main__':
    main()
