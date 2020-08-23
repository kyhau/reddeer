"""
Print authorization details of User, Role, Group, LocalManagedPolicy, and/or AWSManagedPolicy in an account.
"""
import json
import logging

from boto3.session import Session

import click

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("botocore").setLevel(logging.CRITICAL)
logging.getLogger("boto3").setLevel(logging.CRITICAL)
logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)

CHOICES = ["User", "Role", "Group", "LocalManagedPolicy", "AWSManagedPolicy"]


@click.command()
@click.option("--filter", "-f", type=click.Choice(CHOICES, case_sensitive=False))
@click.option("--profile", "-p", help="AWS profile name.")
def main(filter, profile):
    kwargs = {"Filter": [filter]} if filter else {}

    session = Session(profile_name=profile)
    paginator = session.client("iam").get_paginator("get_account_authorization_details")
    for page in paginator.paginate(**kwargs):
        for k, v in page.items():
            if v and k not in ["ResponseMetadata", "IsTruncated"]:
                print(json.dumps(page[k], default=str, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
