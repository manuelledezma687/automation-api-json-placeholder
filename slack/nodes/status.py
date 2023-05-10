import os
from typing import Tuple

import xmltodict


class Status:

    def get_status(self, job_status) -> Tuple[str, str]:
        map_status = {
            "Succeeded": ("SUCCESSFUL", "#086904"),
            "Failed": ("FAILED", "#f70505"),
            "Canceled": ("CANCELLED", "#f77e05")
        }
        return map_status.get(job_status)

    def filter_file_report(self):
        report = {}
        with open('./testResult.xml', 'r', encoding='utf-8') as file:
            my_xml = file.read()
            report = xmltodict.parse(my_xml)['testsuites']
            timestamp = report['testsuite']['@timestamp']
            time = float(report['testsuite']['@time'])
            tests = int(report['testsuite']['@tests'])
            skipped = int(report['testsuite']['@skipped'])
            errors = int(report['testsuite']['@errors'])
            failures = int(report['testsuite']['@failures'])
            passed = tests - skipped - errors - failures
            print(f'Tests: {tests}')
            print(f'Passed: {passed}')
            print(f'Skipped: {skipped}')
            print(f'Errors: {errors}')
            print(f'Failures: {failures}')
        return report
