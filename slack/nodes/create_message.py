from typing import Tuple
from slack.nodes.urls import Urls


class CreateMessage:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_status(self, job_status) -> Tuple[str, str]:
        map_status = {
            "success": ("SUCCESSFUL", "#086904"),
            "failed": ("FAILED", "#f70505"),
            "canceled": ("CANCELLED", "#f77e05")
        }
        return map_status.get(job_status, ("UNKNOWN", "#000000"))

    def create_title(self, args, job_status):
        urls = Urls(args=args)
        title = f"{job_status}: "
        if args.organization:
            title += f"{args.organization} "
        if args.project:
            title += f"{args.project} "
        if args.run_id:
            title += f"{args.run_id}"
        title += f"\n<{urls.report_link(args)}|(Report)>"
        return title

    def create_subtitle(self, args):
        subtitle = ""
        subtitle += f"Commit #: {args.commit}\n"
        # subtitle += f"Tests: {args.tests}\n"
        # subtitle += f"Environment: {args.environment}\n"
        # if args.product:
        #     subtitle += f"{args.product.title()} "
        # if (args.suite or args.product) and get_version(args.suite, args.environment):
        #     subtitle += f"- Version: {get_version(args.suite, args.environment)} "
        return f"{subtitle}\n"

    def create_message(self, args, report: dict):
        tests = int(report['testsuite'].get('@tests', 0))
        skipped = int(report['testsuite'].get('@skipped', 0))
        errors = int(report['testsuite'].get('@errors', 0))
        failures = int(report['testsuite'].get('@failures', 0))
        time = float(report['testsuite']['@time'])
        formatted_time = ''
        if time > 60:
            minutes = round(time/60)
            seconds = round(time) % 60
            formatted_time = f'{minutes}:{seconds:02d} min'
        else:
            formatted_time = f'{round(time, 3)} s'
        if int(report['testsuite']['@tests']) > 0 and int(report['testsuite']['@errors']) + int(report['testsuite']['@failures']) == 0:
            result, color = self.get_status('success')
        else:
            result, color = self.get_status('failed')
        results = f"*-> Tests run: {tests}, Failures: {failures}, Errors: {errors}, Skipped: {skipped}*\nTotal time: {formatted_time}"
        message = {
            "channel": args.slack_channel,
            "attachments": [
                {
                    "color": color,
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": self.create_title(args=args, job_status=result)
                            }
                        },
                        {
                            "type": "divider"
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": self.create_subtitle(args=args)
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*Results:*\n{results}"
                            }
                        }
                    ]
                }
            ]
        }

        return message
