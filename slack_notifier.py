import argparse
import pprint
from slack.nodes.status import Status
from slack.nodes.create_message import CreateMessage
from slack.nodes.send_slack import SendSlack


def create_args():
    parser = argparse.ArgumentParser(description='Send notifications slack')
    parser.add_argument('-s', '--slack-channel', dest='slack_channel',
                        type=str, help='Slack channel name', required=True)
    parser.add_argument('-js', '--job-status', dest='job_status',
                        type=str, help='Azure job status', required=True)
    parser.add_argument('-ri', '--run-id', dest='run_id',
                        type=str, help='Azure run id', required=True)
    parser.add_argument('-p', '--project', dest='project',
                        type=str, help='Azure project', required=True)
    parser.add_argument('-o', '--organization', dest='organization',
                        type=str, help='Azure organization', required=True)
    parser.add_argument('-c', '--commit', dest='commit',
                        type=str, help='Commit', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    args = create_args()
    print("Args:")
    pp.pprint(vars(args))
    print("=" * 50)
    status = Status()
    test_report = status.filter_file_report()
    message = CreateMessage()
    message_slack = message.create_message(args=args,report=test_report)
    print(message_slack)
    send_slack = SendSlack()
    send_slack.send_slack(message_slack=message_slack)
