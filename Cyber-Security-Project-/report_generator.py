# report_generator.py

from datetime import datetime


def generate_txt_report(data):

    import os

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:

        file.write("WEBSITE SECURITY REPORT\n")
        file.write("=" * 50 + "\n")

        file.write(f"Scan Date : {datetime.now()}\n")
        file.write(f"Website   : {data['url']}\n")
        file.write(f"Score     : {data['score']}\n")
        file.write(f"Rating    : {data['rating']}\n\n")

        file.write("SSL DETAILS\n")
        file.write(str(data['ssl']))
        file.write("\n\n")

        file.write("HEADERS\n")

        for k, v in data['headers'].items():
            file.write(f"{k}: {v}\n")

        file.write("\nRECOMMENDATIONS\n")

        for rec in data['recommendations']:
            file.write(f"- {rec}\n")

    return filename