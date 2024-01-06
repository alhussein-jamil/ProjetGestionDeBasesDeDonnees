import argparse

import yaml
from mysql.connector import MySQLConnection

from src.data_visualization import run_app
from src.plotting import plot
from src.query import Query

# Application principale
if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="MySQL username", default="User", type=str)
    parser.add_argument(
        "-a", "--app", help="Do not Run the App", default=True, action="store_false"
    )
    parser.add_argument(
        "-p", "--plots", help="Generate plots", default=False, action="store_true"
    )
    args = parser.parse_args()

    user = args.user

    config_dict = yaml.safe_load(open("config/query_config.yaml"))
    user_config = yaml.safe_load(open("config/user_config.yaml"))

    mysql_connection = MySQLConnection(
        **user_config[user],
    )

    queries_texts = []
    with open("data/modified_queries.sql") as f:
        for line in f:
            if "-- Query" in line:
                queries_texts.append("")
            queries_texts[-1] += line

    query_instance_list = []

    for i, query_text in enumerate(queries_texts):
        if f"query{i+1}" in config_dict:
            query_instance_list.append(
                Query(query_text, config_dict[f"query{i+1}"], mysql_connection)
            )
    if args.plots:
        plot(connection=mysql_connection)
    else:
        if args.app:
            run_app(query_instance_list)
