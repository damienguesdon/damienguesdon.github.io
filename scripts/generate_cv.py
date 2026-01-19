import yaml
import jinja2
import datetime
import os
import argparse


def calculate_experience(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    years = today.year - start_date.year
    if (today.month, today.day) < (start_date.month, start_date.day):
        years -= 1
    return years


def render_cv(data_file, template_file, output_file, overrides=None, force_lang=None):
    with open(data_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if overrides:
        with open(overrides, "r", encoding="utf-8") as f:
            override_data = yaml.safe_load(f)
            if "summary" in override_data:
                data["summary"].update(override_data["summary"])
            if "skills_highlight" in override_data:
                data["skills_highlight"] = override_data["skills_highlight"]

    xp_years = calculate_experience("2005-01-01")
    data["xp_years"] = xp_years
    data["serial_version"] = datetime.datetime.now().strftime("v%Y%m%d-%H%M")
    data["force_lang"] = force_lang

    # Process summary variables
    for lang in data["summary"]:
        data["summary"][lang] = data["summary"][lang].replace(
            "{{ xp_years }}", str(xp_years)
        )

    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_file)

    output = template.render(**data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"CV generated successfully: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CV from YAML and Template")
    parser.add_argument(
        "--target", type=str, default=None, help="Target specific job (e.g. skaelia)"
    )
    parser.add_argument(
        "--lang", type=str, default=None, help="Force language (fr or en)"
    )
    parser.add_argument(
        "--output", type=str, default="index.html", help="Output filename"
    )
    args = parser.parse_args()

    data_path = "data/cv.yaml"
    template_path = "src/templates/cv_template.html"

    overrides_path = (
        f"data/cv_{args.target}.yaml"
        if args.target and os.path.exists(f"data/cv_{args.target}.yaml")
        else None
    )

    render_cv(
        data_path,
        template_path,
        args.output,
        overrides=overrides_path,
        force_lang=args.lang,
    )
