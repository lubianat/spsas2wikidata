import pandas as pd
from wdcuration import render_qs_url
from pathlib import Path

HERE = Path(__file__).parent.resolve()
RESULTS = HERE.parent.joinpath("results").resolve()


def main():

    print(
        render_qs_url(
            add_members_to_organization(
                curated_sheet_path=RESULTS.joinpath("curation_sheet.tsv"),
                organization_id="Q116505289",
                reference_url="https://web.archive.org/web/20230131113424/https://www.itps.org.br/membros",
            )
        )
    )


def add_members_to_organization(curated_sheet_path, organization_id, reference_url):
    df = pd.read_csv(curated_sheet_path, dtype={"id": object})
    qs = ""
    for i, row in df.iterrows():
        if row["wikidata_id"] != "NONE":
            property = "P463"
            wikidata_id = row["wikidata_id"]
            speaker_name = row["name"]
            qs += (
                f'{wikidata_id}|{property}|{organization_id}|S854|"{reference_url}"'
                + "\n"
            )
            qs += f'{wikidata_id}|Aen|"{speaker_name}"' + "\n"
    return qs


def add_organizers_to_event(curated_sheet_path, event_id, reference_url):
    df = pd.read_csv(curated_sheet_path, dtype={"id": object})
    qs = ""
    for i, row in df.iterrows():
        if row["wikidata_id"] != "NONE":
            property = "P664"
            wikidata_id = row["wikidata_id"]
            speaker_name = row["name"]
            qs += f'{event_id}|{property}|{wikidata_id}|S854|"{reference_url}"' + "\n"
            qs += f'{wikidata_id}|Aen|"{speaker_name}"' + "\n"
    return qs


def add_speakers_to_event(curated_sheet_path, event_id, reference_url):
    df = pd.read_csv(curated_sheet_path, dtype={"id": object})
    qs = ""
    for i, row in df.iterrows():
        if row["wikidata_id"] != "NONE":
            property = "P823"
            wikidata_id = row["wikidata_id"]
            speaker_name = row["name"]
            qs += f'{event_id}|{property}|{wikidata_id}|S854|"{reference_url}"' + "\n"
            qs += f'{wikidata_id}|Aen|"{speaker_name}"' + "\n"
    return qs


if __name__ == "__main__":
    main()
