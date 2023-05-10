
class Urls:
    def __init__(self, args):
        self.args = args
    
    def report_link(self, args):
        return f'https://dev.azure.com/{args.organization}/{args.project}/_build/results?buildId={args.run_id}'
